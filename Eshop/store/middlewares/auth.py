from django.shortcuts import redirect

def auth_middleware(get_response):

    def middleware(request):
        print(middleware)
        returnUrl = request.META['PATH_INFO'] # this will return path of previous Url
        if not request.session.get('customer'):
            # return redirect('login')
            return redirect(f'login?return_url={returnUrl}')
        
        response = get_response(request)
        return response
        
    return middleware
        
