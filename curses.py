import responder

api = responder.API()

@api.route("/")
def hello_world(req,resp):
	resp.text = "hello, world!"

@api.route("/hello/{who}/html")
def hello_html(req,resp,*,who):
	resp.content = api.template('hello.html',who=who)

api.run()
