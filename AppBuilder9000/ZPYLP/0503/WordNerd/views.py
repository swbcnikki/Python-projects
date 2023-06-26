from django.shortcuts import render, get_object_or_404, redirect, Http404
from .forms import wordform
from .models import word

# this view renders home page
def WordNerd_home(request):
    return render(request, 'wordnerd/WordNerd_home.html')
# this view validates the form and pushes data to the RDB
def WordNerd_createword(request):
    wordForm = wordform()
    if request.method == 'POST':
        print(request.POST)
        wordForm = wordform(request.POST)
        if wordForm.is_valid():
            wordForm.save()
    context = {'wordForm': wordForm}
    return render(request, 'wordnerd/WordNerd_createword.html', context)
# this view returns a list of the word names in the data base
def WordNerd_viewdata(request):
    allWords = word.objects.all
    context = {
        'allWords': allWords
    }
    return render(request, "wordnerd/WordNerd_viewdata.html", context)
#uses primary key as a filter tag for selecting the chosen word and display corresponding details
def WordNerd_worddetails(request, pk):
    pk = int(pk)
    word_get = word.objects.filter(pk=pk)
    context = {'word_get': word_get}
    return render(request, "wordnerd/WordNerd_worddetails.html", context)


# allows user to update word entries
def WordNerd_wordupdate(request, pk):
    try:
        old_data = get_object_or_404(word, pk = pk)
    except Exception:
        raise Http404('Does Not Exist')
    if request.method =='POST':
        Uform = wordform(request.POST, instance =old_data)

        if Uform.is_valid():
            Uform.save()
            context = {
                'Uform': Uform
            }
            return render(request, 'wordnerd/WordNerd_wordupdate.html', context)
    else:
        Uform = wordform(instance=old_data)
        context = {
            'Uform': Uform
        }
        return render(request, 'wordnerd/WordNerd_wordupdate.html', context)
# allows user to delete a word
def WordNerd_worddelete(request, pk):
    data = get_object_or_404(word, pk=pk)
    if request.method == 'POST':
        data.delete()
        return render(request, "wordnerd/WordNerd_confirmdelete.html")
    else:
        return render(request, 'wordnerd/WordNerd_worddelete.html')


