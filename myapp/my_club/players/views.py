from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import admin
from django.urls import path
from django.template import loader
from .models import Player



# def players(request):
#     template = loader.get_template('first.html')
#     return render(request, 'first.html')
    #return HttpResponse(template.render())

def players(request):
  myplayers = Player.objects.all().values()
  template = loader.get_template('all_players.html')
  context = {
    'myplayers': myplayers,
  }
  return HttpResponse(template.render(context, request))


def details(request, id):
  myplayer = Player.objects.get(id=id)
  template = loader.get_template('details.html')
  context = {
    'myplayer': myplayer,
  }