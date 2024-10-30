from django.shortcuts import render, redirect


def auth_middleware(get_response):
    # One-time configuration and initialization.

    def middleware(request):
        if (request.path == '/Accounts/profile/') and (request.session.get('id') is None) :
                return redirect('/Accounts/login/')
        
        if (request.path == '/Accounts/login/' or request.path == '/Accounts/') and (request.session.get('id') is not None) :
                return redirect('/Accounts/profile/')
        

        response = get_response(request)

        return response

    return middleware