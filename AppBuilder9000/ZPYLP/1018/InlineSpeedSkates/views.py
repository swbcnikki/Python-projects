from django.shortcuts import render, get_object_or_404, redirect
from .forms import ReviewForm
# imports data from the model Review
from .models import Review


# Displays the Home page
def InlineSpeedSkates_Home(request):
    return render(request, 'skates_home.html')


# Creates new inline skate review record and writes to database
def Review_Create(request):
    form = ReviewForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('Review_Create')
    else:
        print(form.errors)
        form = ReviewForm()
        context = {
            'form': form,
        }
    return render(request, 'skates_create.html', context)


# Retrieves and displays all condensed records from database via skates_display.html
def Review_Display(request):
    records = Review.objects.all().order_by('date')
    return render(request, 'skates_display.html', {'records': records})

# Retrieves expanded record details from database via hyperlink in skates_display.html
# and launches skates_display.html
def Review_Details(request, pk):
    details = get_object_or_404(Review, pk=pk)
    context = {'details': details}
    return render(request, 'skates_details.html', context)
