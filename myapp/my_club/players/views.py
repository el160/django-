from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import admin
from django.urls import path
from django.template import loader



# def players(request):
#     #template = loader.get_template('first.html')
#    return render(request, 'players/first.html')

def players(request):
    print("Hello World")
    return HttpResponse("Hello world!")
