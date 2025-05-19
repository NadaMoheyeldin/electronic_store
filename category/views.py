from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
#function based view
def category_list(request):
    return HttpResponse('<h1>category_list</h1>')

def category_add(request): #request.method => GET/POST
                           #request.path => its path
    return HttpResponse('<h1>category added</h1>')

def category_update(request,id):
    return HttpResponse(f'<h1>category{id}</h1>')