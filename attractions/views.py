from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home_view(request):
    return HttpResponse(content='<h1>Home</h1>')
