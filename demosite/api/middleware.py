
class WunderPreviewDemoMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.
        request.META['HTTP_HOST'] = request.META['HTTP_X_FORWARDED_HOST']

        response = self.get_response(request)

        # Code to be executed for each request/response after
        # the view is called.

        return response
