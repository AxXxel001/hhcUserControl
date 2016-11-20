import tornado.web
import tornado.ioloop
import pystache
from pystache.loader import Loader
from pystache.renderer import Renderer
from os.path import abspath

class PartialsLoader(object):
	def __init__(self):
		self.loader = Loader(extension="html", search_dirs=["template/partials"])

	def get(self, template_name):
		return self.loader.load_name(template_name)

renderer = Renderer(
	file_extension="html",
	search_dirs=["template"],
	partials=PartialsLoader()
)

class HelloWorldHandler(tornado.web.RequestHandler):
	def get(self):
		data = {}
		data["css_main"] = "main.css"
		data["css_navbar"] = "navbar.css"
		data["css_content"] = "content.css"
		data["css_footer"] = "footer.css"
		html = renderer.render_name("main", data)
		self.write(html)

settings = {
	"debug": True
}
handlers = [
	(r"/", HelloWorldHandler),
	(r"/static/(.*)", tornado.web.StaticFileHandler, {"path": "static"}),
]
app = tornado.web.Application(handlers, **settings)
app.listen(4455)
print "Listening on localhost:8888..."
try:
	tornado.ioloop.IOLoop.current().start()
except KeyboardInterrupt:
	pass
print "Done."
