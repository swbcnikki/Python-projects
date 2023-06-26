from django.shortcuts import render, get_object_or_404, redirect
from .models import Review
from .forms import ReviewForm


# Render Home page
def home(request):
    return render(request, "VideoGameReviews/gamereviews_home.html")


# Render Add page and allows it to modify db
def add_review(request):
    form = ReviewForm(data=request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('gamereviews_addreview')
    context = {'form': form, }
    return render(request, 'VideoGameReviews/gamereviews_addreview.html', context)


# Display db items
def view_review(request):
    reviews = Review.objects.all()
    return render(request, 'VideoGameReviews/gamereviews_displayitems.html', {'reviews': reviews})


# Allows data for one item to be viewed
def review_details(request, pk):
    details = Review.objects.get(pk=pk)
    return render(request, "VideoGameReviews/gamereviews_details.html", {'details': details})


# Delete db items
def review_delete(request, pk):
    item = get_object_or_404(Review, pk=pk)
    form = ReviewForm(data=request.POST or None, instance=item)
    if request.method == 'POST':
        item.delete()
        return redirect('gamereviews_displayitems')
    return render(request, 'VideoGameReviews/gamereviews_delete.html', {'item': item, 'form': form})


# Edit db items
def review_edit(request, pk):
    item = get_object_or_404(Review, pk=pk)
    form = ReviewForm(data=request.POST or None, instance=item)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('gamereviews_displayitems')
    content = {'form': form}
    return render(request, 'VideoGameReviews/gamereviews_edit.html', content)
