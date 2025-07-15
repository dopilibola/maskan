from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def login2(request):
    return render(request, 'login2.html')