from werkzeug.wrappers import Request, Response, ResponseStream


class middleware():
    '''
    Simple WSGI middleware
    '''

    def __init__(self, app):
        self.app = app
        self.userName = 'TestUser'
        self.password = 'TestPass'

    def __call__(self, environ, start_response):
        request = Request(environ)
        userName = request.authorization['username']
        password = request.authorization['password']

        # these are hardcoded for demonstration
        # verify the username and password from some database or env config variable
        if userName == self.userName and password == self.password:
            environ['user'] = {'name': 'Test User'}
            return self.app(environ, start_response)

        res = Response('Authorization failed',
                       mimetype='text/plain', status=401)
        return res(environ, start_response)