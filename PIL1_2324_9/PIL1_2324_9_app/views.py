from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.http import HttpResponse
# Create your views here.
def home(request):
    #return  HttpResponse("<h2>Welcome to my app</h2>")#render(request,'index.html')
    template = loader.get_template('home.html')
    return HttpResponse(template.render())

