from django.shortcuts import render, redirect, get_object_or_404
from .models import VideoGames
from .forms import VideoGamesForm


# render home page

def VG_home(request):
    # render function takes argument  - request
    # and return HTML as response
    return render(request, 'VideoGameApp/Video-Game-App-Home.html')


def videoGames_add(request):
    addForm = VideoGamesForm(data=request.POST or None)
    if request.method == 'POST' and addForm.is_valid():
        addForm.save()
        return redirect('VideoGameAppHome')
    content = {'addForm': addForm}
    return render(request, "VideoGameApp/VGA_Forms.html", content)

def Display_Games(request):
    games = VideoGames.objects.all()
    content = {'games': games}
    return render(request, 'VideoGameApp/VGA_Details.html', content)


def Retrieve_DetailView(request, _id):
    try:
        data = VideoGames.objects.get(id=_id)
    except VideoGames.DoesNotExist:
        raise Http404('Data does not exist')

    return render(request, 'VideoGameApp/RetDeets.html', {'data': data})


def UpdateView(request, _id):
    try:
        old_data = get_object_or_404(VideoGames, id=_id)
    except Exception:
        raise Http404('Does Not Exist')

    if request.method == 'POST':
        form = VideoGamesForm(request.POST, instance=old_data)

        if form.is_valid():
            form.save()
            return redirect(f'/data/{_id}')

    else:

        form = VideoGamesForm(instance=old_data)
        context = {
            'form': form
        }
        return render(request, 'VideoGameApp/VGA_updates.html', context)


def DeleteView(request, _id):
    try:
        data = get_object_or_404(VideoGames, id=_id)
    except Exception:
        raise Http404('Does Not Exist')

    if request.method == 'POST':
        data.delete()
        return redirect('/data')
    else:
        return render(request, 'VideoGameApp/VGA_delete.html')

