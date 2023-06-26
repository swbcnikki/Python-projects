from django.shortcuts import render, redirect, get_object_or_404
from .models import Entry
from .forms import EntryForm



# Details Page
def post_details(request, pk):
    Entryinfo = get_object_or_404(Entry, pk=int(pk))
    context = {'Entryinfo': Entryinfo}
    return render(request, 'Entries/Details.html', context)


# Edit Page
def edit_post(request, pk):
    Entryinfo = get_object_or_404(Entry, pk=int(pk))
    form = EntryForm(data=request.POST or None, instance=Entryinfo)
    if request.method == 'POST':
        if form.is_valid():
            form2 = form.save(commit=False)
            form2.save()
            return redirect('DetailsPage', pk)
        else:
            print(form.errors)
    else:
        return render(request, 'Entries/Edit.html', {'Entryinfo': Entryinfo, 'form': form})

# Delete
def delete_post(request, pk):
    Entryinfo = get_object_or_404(Entry, pk=int(pk))
    #POST Request
    if request.method == 'POST':
        #confirming delete
        Entryinfo.delete()
        return redirect('DisplayPage')
    context = {'Entryinfo': Entryinfo}
    return render(request,'Entries/Delete.html', context)




# Home Page
def Index(request):  #home page - takes in a parameter called request,


    return render(request, 'Entries/Index.html')   #used to display a template , 1st argument is the request, 2nd argument is the template,3rd is context

# Main display page
def Display(request):

    entries = Entry.objects.order_by('-date_posted')

    context = {'entries': entries}

    return render(request, 'Entries/Display.html', context)

# Add entry page
def Add(request):
    if request.method == 'POST':    # checks to see if the form is a post request ( if they actually hit submit )
        form = EntryForm(request.POST)  # captures data passed in

        if form.is_valid():
            form.save()
            return redirect('DisplayPage')   #retuns user to homepage
    else:

        form = EntryForm()

    context = {'form' : form}

    return render(request, 'Entries/Add.html', context)