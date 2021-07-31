from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def goodmornig_view(request):
    return HttpResponse('<h1> good morning veera</h1>')
def goodafternoon_view(request):
    return HttpResponse('<h1>good afternoon</h1>')
def goodevening_view(request):
    return HttpResponse('<h1>good evening veera</h1>')
