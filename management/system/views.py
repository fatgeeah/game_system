from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse
from .models import Gamer , Games
from .forms import GamerForm

# Create your views here.

def search_games(request):
         if request.method=="POST":
          searched = request.POST['searched']
          allgamers =  Gamer.objects.filter(gamer_games__contains=searched)  
          return render(request, 'system/search_games.html' ,
                        {'searched':searched,
                         'allgamers':allgamers})
         else:
               return render(request, 'system/search_games.html' ,{})


def index(request):
    return render(request, 'system/index.html' , {
        'gamers': Gamer.objects.all()
    })
    
def show_games(request):
    return render(request, 'system/show_games.html' , {
        'games': Games.objects.all()
    })    
    
def add_games(request):
    if request.method == 'POST':
        game_names = request.POST.get('games_name')  # Fix the field name
        game_thumbnails = request.FILES.get('gameThumbnails')
        video = request.FILES.get('video')

        game = Games(game_names=game_names, gameThumbnails=game_thumbnails, video=video)
        game.save()

        return redirect('add_games')

    return render(request, 'system/add_games.html')

def view_gamer(request, id):
     gamer = Gamer.objects.get(pk=id)
     return HttpResponseRedirect(reverse('index'))

def add(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        email = request.POST.get('email')
        games = request.POST.get('games')

        if username == firstname:
            return HttpResponse('Username and first name cannot be the same')
        else:
            # Create a new Gamer instance
            new_gamer = Gamer(
                gamer_username=username,
                gamer_first_name=firstname,
                gamer_last_name=lastname,
                email=email,
                gamer_games=games
            )
            new_gamer.save()

            # Optionally, you can also create a corresponding User object
            # user = User.objects.create_user(username=username, email=email, password=games)

            return redirect('index')

    return render(request, 'system/add.html')
from django.shortcuts import render

def edit(request, id):
    gamer = Gamer.objects.get(pk=id)
    form = GamerForm(instance=gamer)

    if request.method == "POST":
        form = GamerForm(request.POST, instance=gamer)
        if form.is_valid():
            form.save()
            return redirect('index')
    return render(request, 'system/edit.html', {'form': form})
   

def delete(request, id):
      if request.method =="POST":
       gamer = Gamer.objects.get(pk=id) 
       gamer.delete()
       return HttpResponseRedirect(reverse('index'))           




