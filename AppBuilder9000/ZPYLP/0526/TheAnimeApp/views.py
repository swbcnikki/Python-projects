from django.shortcuts import render
from .models import Review
from .forms import ReviewForm
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404


def AnimeHome(request):
    return render(request, 'TheAnimeApp/AnimeHome.html', )


def AnimeReviews(request):
    context = {}
    all_reviews = Review.objects.all
    return render(request, 'TheAnimeApp/AnimeReviews.html', {'all': all_reviews}, context)


def AnimeCreate(request):
    if request.method == "POST":
        form = ReviewForm(request.POST or None)
        if form.is_valid():
            form.save()
        else:
            messages.success(request, ('Opps, There was an error in your form! Please try again.'))
            return redirect('AnimeCreate')
        messages.success(request, ("Thank you, Review has been added here!"))
        return redirect('AnimeReviews')
    else:
        return render(request, 'TheAnimeApp/AnimeCreate.html')


def AnimeDetails(request, pk):
    anime_detail = get_object_or_404(Review, pk=pk)
    all_detail = {'anime_detail': anime_detail}
    context = all_detail
    return render(request, "TheAnimeApp/AnimeDetails.html", context)


def AnimeDisplay(request):
    all_detail = Review.objects.all()
    context = {'all_detail': all_detail}
    return render(request, "TheAnimeApp/AnimeDisplay.html", context)


