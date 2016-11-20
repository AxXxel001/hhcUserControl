import tornado.web
import tornado.ioloop

class HelloWorldHandler(tornado.web.RequestHandler):
	def get(self):
		self.write("Hello, World!")

app = tornado.web.Application([
	(r"/", HelloWorldHandler),
])
app.listen(4455)
print "Listening on localhost:8888..."
try:
	tornado.ioloop.IOLoop.current().start()
except KeyboardInterrupt:
	pass
print "Done."
