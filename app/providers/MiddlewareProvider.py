''' A MiddlewareProvider Service Provider '''
from masonite.provider import ServiceProvider
from config import middleware

class MiddlewareProvider(ServiceProvider):

    def register(self):
        self.app.bind('HttpMiddleware', middleware.HTTP_MIDDLEWARE)

    def boot(self):
        pass
