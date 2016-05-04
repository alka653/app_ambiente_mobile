from django.http import HttpResponse
from tastypie.http import HttpMethodNotAllowed
from tastypie.exceptions import ImmediateHttpResponse
from tastypie.resources import ModelResource, csrf_exempt

class CorsResourceBase(ModelResource):
	def error_response(self, *args, **kwargs):
		response = super(CorsResourceBase, self).error_response(*args, **kwargs)
		return self.add_cors_headers(response, expose_headers=True)

	def add_cors_headers(self, response, expose_headers=False):
		response['Access-Control-Allow-Origin'] = '*'
		response['Access-Control-Allow-Headers'] = 'content-type, authorization'
		if expose_headers:
			response['Access-Control-Expose-Headers'] = 'Location'
		return response

	def create_response(self, *args, **kwargs):
		response = super(CorsResourceBase, self).create_response(*args, **kwargs)
		return self.add_cors_headers(response)

	def post_list(self, request, **kwargs):
		response = super(CorsResourceBase, self).post_list(request, **kwargs)
		return self.add_cors_headers(response, True)

	def post_detail(self, request, **kwargs):
		response = super(CorsResourceBase, self).post_list(request, **kwargs)
		return self.add_cors_headers(response, True)

	def put_list(self, request, **kwargs):
		response = super(CorsResourceBase, self).put_list(request, **kwargs)
		return self.add_cors_headers(response, True)    

	def put_detail(self, request, **kwargs):
		response = super(CorsResourceBase, self).put_detail(request, **kwargs)
		return self.add_cors_headers(response, True)
		
	def method_check(self, request, allowed=None):
		if allowed is None:
			allowed = []

		request_method = request.method.lower()
		allows = ','.join(map(lambda s: s.upper(), allowed))

		if request_method == 'options':
			response = HttpResponse(allows)
			response['Access-Control-Allow-Origin'] = '*'
			response['Access-Control-Allow-Headers'] = 'Content-Type, Authorization'
			response['Access-Control-Allow-Methods'] = "GET, PUT, POST, PATCH"
			response['Allow'] = allows
			raise ImmediateHttpResponse(response=response)

		if not request_method in allowed:
			response = HttpMethodNotAllowed(allows)
			response['Allow'] = allows
			raise ImmediateHttpResponse(response=response)
		return request_method

	def wrap_view(self, view):
		@csrf_exempt
		def wrapper(request, *args, **kwargs):
			request.format = kwargs.pop('format', None)
			wrapped_view = super(CorsResourceBase, self).wrap_view(view)
			return wrapped_view(request, *args, **kwargs)
		return wrapper