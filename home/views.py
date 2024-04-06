from django.shortcuts import render, HttpResponse


# Create your views here.


def index(request):   
    return render(request, 'index.html')
    #return HttpResponse('welcome to about page')

def about(request):
    #return render(request, 'about.html')
    return HttpResponse('welcome to about page')

def services(request):
    return HttpResponse('welcome to services page')

def contact(request):
    return HttpResponse('welcome to contact page')

