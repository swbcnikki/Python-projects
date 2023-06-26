from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect
from .forms import CharacterForm
from .models import Character


def home(request):
    return render(request, 'swu_home.html')


def sources(request):
    return render(request, 'swu_sources.html')


def characters(request):
    form = CharacterForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect("swu_characters")
        else:
            form = CharacterForm()
    return render(request, 'swu_characters.html', {'form': form})


def characters_list(request):
    char_list = Character.objects.all()
    return render(request, 'swu_charlist.html', {'char_list': char_list})


def character_details(request, id):
    char_list = get_object_or_404(Character, id=id)
    return render(request, "swu_details.html", {
        'Name': char_list.Name_of_Character,
        'First_Appearance': char_list.First_Appearance,
        'Race': char_list.Race_Type,
        'Affiliation': char_list.Affiliation,
        'Details': char_list.Additional_Details,
    })


def edit_char_list(request, id):
    char_list = get_object_or_404(Character, id=id)
    form = CharacterForm(request.POST or None, instance=char_list)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect('/StarWarsUniverse/' + id)
    return render(request, "swu_edit.html", {"form": form})


def delete_character(request, id):
    char_list = get_object_or_404(Character, id=id)
    form = CharacterForm(request.POST or None, instance=char_list)
    if request.method == "POST":
        char_list.delete()
        return HttpResponseRedirect('/StarWarsUniverse/characters_list')
    return render(request, "swu_delete.html", {"form": form})
