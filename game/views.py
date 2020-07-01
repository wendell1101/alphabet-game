from django.shortcuts import render
from game.models import GameImage,Choice

def game(request):
  
  
    return render(request,'game/game.html')
