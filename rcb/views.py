from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def viratkohli(request):
    return HttpResponse('<h2>viratkohli is the captain of rcb<h2>')


