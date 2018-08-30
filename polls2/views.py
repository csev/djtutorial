from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. Jane Instructor / 1ff1de77 is the polls index.")

