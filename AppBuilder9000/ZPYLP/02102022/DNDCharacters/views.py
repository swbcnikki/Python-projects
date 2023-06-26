from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect
from .forms import CharacterForm
from .models import Characters


def dnd_characters_home(request):
    return render(request, 'DNDCharacters/dnd_characters_home.html')

def dnd_character_lookup(request):
    characters = Characters.objects.all()
    return render(request, 'DNDCharacters/dnd_character_lookup.html', {'characters': characters})

def dnd_characters_howto(request):
    return render(request, 'DNDCharacters/dnd_characters_HowTo.html')

def createCharacter(request):
    form = CharacterForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('dnd_character_lookup')
    else:
        print(form.errors)
        form = CharacterForm()
    context = {
        'form': form,
    }
    return render(request, 'DNDCharacters/dnd_characters_Creation.html', context)

def dnd_characters_classdescript(request):
    return render(request, 'DNDCharacters/dnd_characters_ClassDescript.html')

def dnd_character_search(request):
    if request.method == "POST":
        searched = request.POST.get('searched', False)
        character = Characters.objects.filter(Character_Name__contains=searched)
        print(searched)
        return render(request, 'DNDCharacters/dnd_character_search.html', {'searched': searched,
                                                                           'character': character})
    else:
        return render(request, 'DNDCharacters/dnd_character_search.html')

def show_character(request, character_id):
    character = Characters.objects.get(pk=character_id)
    return render(request, 'DNDCharacters/dnd_show_character.html', {'character': character})

def update_character(request, character_id):
    character = Characters.objects.get(pk=character_id)
    form = CharacterForm(request.POST or None, instance=character)
    if form.is_valid():
        form.save()
        return redirect('dnd_character_lookup')
    return render(request, 'DNDCharacters/dnd_character_update.html', {'character': character, 'form': form})

def delete_character(request, character_id):
    character = Characters.objects.get(pk=character_id)
    information = {'characters': character}
    if request.method == "POST":
        character.delete()
        return redirect('dnd_character_lookup')
    return render(request, 'DNDCharacters/delete_confirm.html', information)

