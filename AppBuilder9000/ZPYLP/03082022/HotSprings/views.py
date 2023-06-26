from django.shortcuts import render, get_object_or_404, redirect
from .form import hotspringsForm
from .models import HotSprings






def hotsprings_home(request):
    # render method takes the request object and template name as arguments
    # returns httpResponse object with rendered text.
    return render(request, 'hotsprings_home.html')


def add_hotsprings(request):
    form = hotspringsForm(data=request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('hotsprings_list')
    else:
        print(form.errors)
        form = hotspringsForm()
        context = {'form' : form}
    return render(request, 'hotsprings_create.html', context)


def list_hotsprings(request):
    hotsprings = HotSprings.objects.all()
    return render(request, 'hotsprings_list.html', {'hotsprings': hotsprings})


def hotsprings_details(request, pk):
    details = get_object_or_404(HotSprings, pk=pk)
    context = {'details': details}
    return render(request, 'hotsprings_details.html', context)



# update view for details
def update_view(request, id):
    # dictionary for initial data with
    # field names as keys
    context = {}

    # fetch the object related to passed id
    obj = get_object_or_404(HotSprings, id=id)

    # pass the object as instance in form
    form = hotspringsForm(request.POST or None, instance=obj)

    # save the data from the form and
    # redirect to detail_view
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/" + id)

    # add form dictionary to context
    context["form"] = form

    return render(request, "update_view.html", context)

