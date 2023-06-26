from django.shortcuts import render, redirect, get_object_or_404
from .models import VideoReviews
from .forms import VideoReviewsForm


def videogamereviews(request):
    content = {}
    return render(request, 'VideoGameReviews/VideoGamesReviews_Home.html', content)


def videoreviews(request):
    all_reviews = VideoReviews.objects.all()
    context = {'all': all_reviews}
    return render(request, 'VideoGameReviews/VideoGamesReviews_Reviews.html', context)


def create(request):
    form = VideoReviewsForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect("VideoGamesReviews_Create")
    context = {"form": form}
    return render(request, "VideoGameReviews/VideoGamesReviews_Create.html", context)


def videodetails(request, pk):
    video_detail = get_object_or_404(VideoReviews, pk=pk)
    all_detail = {'video_detail': video_detail}
    context = all_detail
    return render(request, "VideoGameReviews/VideoGamesReviews_Details.html", context)
