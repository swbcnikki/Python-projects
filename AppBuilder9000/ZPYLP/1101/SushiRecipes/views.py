from django.shortcuts import render, redirect, get_object_or_404
from .forms import SushiForm
from .models import SushiRecipes


def sushi_recipes_home(request):
    return render(request, 'SushiRecipes/Sushi_Recipes_Home.html')


def sushi_recipes_view(request):
    view = SushiRecipes.objects.all()
    return render(request, 'SushiRecipes/Sushi_Recipes_View.html', {'view': view})


def sushi_recipes_create(request):
    form = SushiForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('Sushi_Recipes_Create')
    else:
        print(form.errors)
        form = SushiForm()
        context = {'form': form}
    return render(request, 'SushiRecipes/Sushi_Recipes_Create.html', context)


def sushi_recipes_details(request, pk):
    details = get_object_or_404(SushiRecipes, pk=pk)
    context = {'details': details}
    return render(request, "SushiRecipes/Sushi_Recipes_Details.html", context)


def sushi_recipes_edit(request, pk):
    edit = get_object_or_404(SushiRecipes, pk=pk)
    form = SushiForm(request.POST or None, instance=edit)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('Sushi_Recipes_View')
    else:
        return render(request, 'SushiRecipes/Sushi_Recipes_Edit.html', {'form': form})


def sushi_recipes_delete(request, pk):
    obj = get_object_or_404(SushiRecipes, pk=pk)
    form = SushiForm(request.POST or None, instance=obj)
    if request.method == 'POST':
        obj.delete()
        return redirect('../../')
    context = {
        "object": obj
    }
    return render(request, 'SushiRecipes/Sushi_Recipes_Delete.html', context)
