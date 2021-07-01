FBV #基于function
    urls:
        path('index/',views.index)
    views:
        def index(request):
            pass
            return render(request,'index.html')

CBV #基于class
    uels:
        path('index',views.Ass.as_view())
    views:
        from django.views import View
        class Ass(View):
            '''
            http_method_names = ['get', 'post', 'put', 'patch', 'delete', 'head', 'options', 'trace']
            '''
            def get(self,request):
                return render(request,'get.html')

            def post(self,request):
                return render(request,'post.html')

'''分发函数
def dispatch(self, request, *args, **kwargs):
    # Try to dispatch to the right method; if a method doesn't exist,
    # defer to the error handler. Also defer to the error handler if the
    # request method isn't on the approved list.
    if request.method.lower() in self.http_method_names:
        handler = getattr(self, request.method.lower(), self.http_method_not_allowed)
    else:
        handler = self.http_method_not_allowed
    return handler(request, *args, **kwargs)
'''
