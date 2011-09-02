import re

def is_hex_or_decimal(str):
	'Return whether the number is hex or decimal'
	print str
	return re.match('^[0123456789abcdefABCDEF]+$', str)

