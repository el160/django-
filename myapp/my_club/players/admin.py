from django.contrib import admin
from .models import Player
 

class PlayerAdmin(admin.ModelAdmin): # for displaying purpose
    list_display = ('firstname','lastname','age')

admin.site.register(Player, PlayerAdmin)
