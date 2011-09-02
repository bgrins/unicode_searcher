#!/usr/bin/env python

import sqlite3
conn = sqlite3.connect('ucd2.sqlite')

import os.path
import re
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
import helpers
from char import Char

from tornado.options import define, options

define("port", default=8888, help="run on the given port", type=int)
define("sqlite3_path", default='ucd2.sqlite', help="sqlite path")


class Application(tornado.web.Application):
	def __init__(self):
		handlers = [
			(r"/", HomeHandler),
			(r"/search/", SearchHandler),
			(r"/char/([^/]+)", CharHandler)
		]
		settings = dict(
			title=u"Find Unicode Characters",
			template_path=os.path.join(os.path.dirname(__file__), "templates"),
			static_path=os.path.join(os.path.dirname(__file__), "static"),
			ui_modules={"Char": CharModule},
			xsrf_cookies=True,
			cookie_secret="11oETzKXQAGaYdkL5gEmGeJJFuYh7EQnp2XdTP1o/Vo=",
			autoescape=None,
			q=None
		)
		tornado.web.Application.__init__(self, handlers, **settings)

		self.db = sqlite3.connect(options.sqlite3_path)

class BaseHandler(tornado.web.RequestHandler):
	@property
	def db(self):
		return self.application.db

class HomeHandler(BaseHandler):
	def get(self):
		self.render("home.html")
		
class SearchHandler(BaseHandler):
	def get(self):
		c = self.db.cursor()
		
		search = self.get_argument("q", None)
		partial = self.get_argument("partial", None)
		
		if not search: self.redirect('/')
		
		if len(search) > 3 and helpers.is_hex_or_decimal(search):
			c.execute('SELECT * FROM ucd where cf=? limit 1', (search,))
		else:
			c.execute("SELECT * FROM ucd where na1 like ? limit 1000", ['%'+search+'%'])
					
		chars = map (Char, c)
		
		if partial: self.render("chars.html", chars=chars)
		else: self.render("results.html", chars=chars, q=search )

class CharHandler(BaseHandler):
	def get(self, id):
		c = self.db.cursor()
		row = c.execute('SELECT * FROM ucd where cf=? limit 1', (id,)).fetchall()
		print row
		 	
		if not row: raise tornado.web.HTTPError(404)
		
		char = Char(row[0]);
		self.render("char.html", char=char, q = char.na1)

class CharModule(tornado.web.UIModule):
	def render(self, char):
		return self.render_string("modules/char.html", char=char)
	
def main():
	tornado.options.parse_command_line()
	http_server = tornado.httpserver.HTTPServer(Application())
	http_server.listen(options.port)
	tornado.ioloop.IOLoop.instance().start()

if __name__ == "__main__":
	main()
