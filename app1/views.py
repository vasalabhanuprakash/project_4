from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def Function(request):
    return HttpResponse('<h1>My name is Bhanu</h1>')

def Function1(request):
    return HttpResponse('<h1>Iam from Andhra Pradesh</h1>')
