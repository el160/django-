from django.shortcuts import render
from django.http import HttpResponse

def players(request):
    return HttpResponse("hey players")
