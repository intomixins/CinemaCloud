from django.shortcuts import render


def google_login(request):
    """ страница входа через гугл"""
    return render(request, 'oauth/google_login.html')
