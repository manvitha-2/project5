from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def ruthuraj(request):
    return HttpResponse('<h2>ruthuraj is the captain of csk<h2>')