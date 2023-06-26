from django.shortcuts import render, redirect, get_object_or_404
from .forms import GuitarForm
from .models import GuitarInfo


# Create your views here.
def home(request):
    return render(request, 'GuitarReviewsApp/GuitarReviewsApp_home.html')


def create(request):
    form = GuitarForm(request.POST or None)
    if request.method == "POST":
        # check if form is valid
        # if so, save
        if form.is_valid():
            form.save()
            return redirect("GuitarReviews_create")

    context = {'form': form}
    return render(request, "GuitarReviewsApp/GuitarReviewsApp_create.html", context)


def review(request):
    reviews = GuitarInfo.objects.all()
    context = {'reviews': reviews}
    return render(request, 'GuitarReviewsApp/GuitarReviewsApp_reviews.html', context)


def details(request, pk):
    info = get_object_or_404(GuitarInfo, pk=pk)
    context = {'info': info}
    return render(request, 'GuitarReviewsApp/GuitarReviewsApp_details.html', context)
