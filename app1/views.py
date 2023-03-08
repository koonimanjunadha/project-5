from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def manjunath(request):
    return HttpResponse('<h1><marque>this is my fifth project</h1>/marque')

def raavan(request):
    return HttpResponse('<h1>sunday is a holiday</h1>')