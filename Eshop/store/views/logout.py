from django.shortcuts import render, redirect
from django.views import View

def logout(request):
    request.session.clear()
    return redirect('homepage')