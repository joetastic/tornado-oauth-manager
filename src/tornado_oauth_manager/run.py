import tornado.web
from oauthlib.oauth2 import WebApplicationServer
from tornado_oauth_manager.oauth import SkeletonValidator


server = WebApplicationServer(SkeletonValidator())


class AuthorizationHandler(tornado.web.RequestHandler):
    def get(self):
        client_id = self.get_argument('client_id')
        scopes, credentials = server.validate_authorization_request(
            self.request.uri, self.request.method,
            self.request.body, self.request.headers)

        self.write('<h1> Authorize access to %s </h1>' % client_id)
        self.write('<form method="POST" action="/authorize">')
        for scope in scopes or []:
            self.write('<input type="checkbox" name="scopes" '
                       'value="%s"/> %s' % (scope, scope))
            self.write('<input type="submit" value="Authorize"/>')

    def post(self):
        scopes = self.get_arguments('scopes')
        credentials = {'user': 'foo'}
        headers, body, status = server.create_authorization_response(
            self.request.uri, self.request.method,
            self.request.body, self.request.headers,
            scopes, credentials)
        self.write(repr((headers, body, status)))


class TokenHandler(tornado.web.RequestHandler):
    def post(self):
        credentials = {'user': 'foo'}
        headers, body, status = server.create_token_response(
            self.request.uri, self.request.method,
            self.request.body, self.request.headers,
            credentials)
        self.set_status(status)
        for key, val in headers.iteritems():
            self.set_header(key, val)
        self.write(body)


class TestResource(tornado.web.RequestHandler):
    def get(self):
        self.write('YOUGOTIT')


def main():
    import tornado.ioloop

    application = tornado.web.Application(
        [
            (r"/authorize", AuthorizationHandler),
            (r"/token", TokenHandler),
            (r"/protected", TestResource),
        ],
        debug=True
    )

    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
