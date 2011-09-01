#!perl -w
use strict;
use warnings;
use DBI;
use IO::File;
use XML::Parser;

my %fields;
my @fields;

my %repl = map { $_ => 1 } qw/
  na dm suc slc stc uc lc tc scf cf
/;

my $dbh = DBI->connect("dbi:SQLite:dbname=ucd2","","");

sub start1 {
  my $expat = shift;
  my $elem = shift;
  my %attrs = @_;

  return unless $elem eq 'char';
  return unless defined $attrs{cp};

  foreach my $key (keys %attrs) {
    push @fields, $key unless $fields{$key}++;
  }
}

my $i = 0;
my $sth;

sub start3 {
  my $expat = shift;
  my $elem = shift;
  my %attrs = @_;
  my @lines;

  return unless $elem eq 'char';
  return unless defined $attrs{cp};

  print "$attrs{cp}\n" if $i % 100 == 0;

  foreach my $name (@fields) {
    my $value = $attrs{$name};
    $value = '' unless defined $value;

    # some values use # to represent the code point
    $value =~ s/#/$attrs{cp}/g if $repl{lc $name};

    push @lines, $value;
  }

  $sth->execute(@lines);

  $dbh->commit if $i++ % 2048 == 0;
}

binmode STDOUT, ':utf8';

my $p1 = XML::Parser->new(Handlers => { Start => \&start1 } );
$p1->parsefile('ucd.all.flat.xml');

my $cts = sprintf q{CREATE TABLE ucd (%s)},
  join(',', map { "$_ TEXT" } @fields);

$dbh->do(q{PRAGMA page_size = 4096});
$dbh->do(q{PRAGMA journal_mode = OFF});
$dbh->do(q{PRAGMA synchronous = OFF});
$dbh->{AutoCommit} = 0;

$dbh->do($cts);

$sth = $dbh->prepare(sprintf "INSERT INTO ucd (%s) VALUES (%s)",
    join(',', @fields), join(',', map { '?' } @fields));

die unless $sth;

my $p2 = XML::Parser->new(Handlers => { Start => \&start3 } );
$p2->parsefile('ucd.all.flat.xml');

$dbh->commit;
$sth->finish;
$dbh->disconnect;



