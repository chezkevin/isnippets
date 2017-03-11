from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.
def index(request):
    context = {'name':'kevin', 'tasks': ['do your hw', 'fall in love', 'save the world']}
    context = {}
    
    return render(request, 'users/index.html', context)

def detail(request):
    return HttpResponse("<h1>This is the detail view!</h1>")

def add(request):
    return HttpResponse("<h1>This is the add view!</h1>")
