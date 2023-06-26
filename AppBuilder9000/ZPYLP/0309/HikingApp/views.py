from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .forms import TrailForm
from .models import Trails
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# render home page
def HikingApp_home(request):
    return render(request, "HikingApp/HikingApp_home.html")


# fxn to create trail
def create_trail(request):
    form = TrailForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('HikingApp_addtrail')
    else:
        print(form.errors)
        form = TrailForm()
    context = {
        'form': form,
    }
    return render(request, 'HikingApp/HikingApp_form.html', context)


# render trail index page
def display_index(request):
    trail_list = Trails.objects.order_by('location').all()
    page = request.GET.get('page', 1)

    paginator = Paginator(trail_list, 15)  # show 15 trails per page
    try:
        trails = paginator.page(page)
    except PageNotAnInteger:
        trails = paginator.page(1)
    except EmptyPage:
        trails = paginator.page(paginator.num_pages)
    return render(request, 'HikingApp/HikingApp_index.html', {'trails': trails})


# render search results from index page
def search_results(request):
    if request.method == 'GET':
        query = request.GET.get('q')

        submitbutton = request.GET.get('submit')

        if query is not None:
            lookups = Q(name__icontains=query) | Q(
                location__icontains=query)  # can lookup trail by name or location only

            results = Trails.objects.order_by('name').filter(
                lookups).distinct()  # distinct() is to avoid duplicate results

            context = {'results': results,
                       'submitbutton': submitbutton}

            return render(request, 'HikingApp/HikingApp_searchresults.html', context)

        else:
            return render(request, 'HikingApp/HikingApp_searchresults.html')

    else:
        return render(request, 'HikingApp/HikingApp_searchresults.html')


# trail details page
def trail_details(request, pk):
    trails = get_object_or_404(Trails, pk=pk)
    return render(request, 'HikingApp/HikingApp_details.html', {'trails': trails})


# edit trail
def edit_trail(request, pk):
    pk = int(pk)
    trails = get_object_or_404(Trails, pk=pk)
    form = TrailForm(data=request.POST or None, instance=trails)
    if request.method == 'POST':
        if form.is_valid():
            form2 = form.save(commit=False)
            form2.save()
            return redirect('HikingApp_details', pk)
        else:
            print(form.errors)
    else:
        context = {'trails': trails, 'form': form}
        return render(request, 'HikingApp/HikingApp_edit.html', context)


#delete trail
def delete_trail(request, pk):
    pk = int(pk)
    trails = get_object_or_404(Trails, pk=pk)
    if request.method == 'POST':
        trails.delete()
        return redirect('HikingApp_index')
    else:
        return redirect('HikingApp_details', pk)