from django.contrib import admin
from .models import Player
# Register your models here.
#admin.site.register(Player)
class PlayerAdmin(admin.ModelAdmin): # for displaying purpose
    list_display = ('firstname','lastname','age')

admin.site.register(Player, PlayerAdmin)
