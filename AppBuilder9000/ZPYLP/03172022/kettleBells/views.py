from django.shortcuts import render,get_object_or_404, redirect
from django.views import generic
from .models import Moves
from .forms import MovesForm


def kettleBells(request):
    return render(request, 'kettleBells/kettleBells_home.html')


def get_moves(request):
    moves_list = Moves.objects.all()
    return render(request, 'kettleBells/kettleBells_exercises.html', {'moves_list': moves_list})


def add_exercise(request):
    form = MovesForm(data=request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('KB_home')
    else:
        print(form.errors)
        form = MovesForm()
    context = {
        'form': form,
    }
    return render(request, 'kettleBells/kettleBells_add.html', context)

def show_moves(request, pk):
    details = get_object_or_404(Moves, pk=pk)
    return render(request, 'kettleBells/kettleBells_details.html', {'details': details})


def delete_move(request, pk):
    item = get_object_or_404(Moves, pk=pk)
    form = MovesForm(data=request.POST or None, instance=item)
    if request.method == 'POST':
        item.delete()
        return redirect('KB_moves')
    context = {"item": item, 'form': form}
    return render(request, "kettleBells/kettleBells_delete.html", context)


def kettleBells_edit(request, pk):
    item = get_object_or_404(Moves, pk=pk)
    form = MovesForm(data=request.POST or None, instance=item)
    if request.method == 'POST':
        if form.is_valid():
            form2 = form.save(commit=False)
            form2.save()
            return redirect('KB_moves')
        else:
            print(form.errors)
    else:
        return render(request, 'kettleBells/kettleBells_edit.html', {'form': form})