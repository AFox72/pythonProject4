from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponseNotFound, HttpResponseForbidden
from django.shortcuts import render, redirect

from .forms import CatForm
from .models import Cat


def cat_list(request):
    if request.user.is_authenticated:
        cats = Cat.objects.filter(owner=request.user)
        context = {
            'cats': cats,
        }
        return render(request, 'cat/cat_list.html', context)
    else:
        return redirect('login')


def create_cat(request):
    if request.method == 'POST':
        form = CatForm(request.POST, instance=None)
        if form.is_valid():
            new_cat = form.save(commit=False)
            new_cat.owner = request.user
            new_cat.save()
            return redirect('cat_list')
    else:
        form = CatForm()
    context = {'form': form}
    return render(request, 'cat/create_cat.html', context)


def edit_cat(request, pk):
    try:
        cat = Cat.objects.get(pk=pk)
    except ObjectDoesNotExist:
        return HttpResponseNotFound("Кот не найден")
    if request.user != cat.owner:
        return HttpResponseForbidden("У вас нет прав на редактирование этого кота")
    if request.method == 'POST':
        form = CatForm(request.POST, instance=cat)
        if form.is_valid():
            form.save()
            return redirect('cat_list')
    else:
        form = CatForm(instance=cat)
    context = {'form': form}
    return render(request, 'cat/edit_cat.html', context)


def delete_cat(request, pk):
    try:
        cat = Cat.objects.get(pk=pk)
    except ObjectDoesNotExist:
        return HttpResponseNotFound("Кот не найден")
    if request.user != cat.owner:
        return HttpResponseForbidden("У вас нет прав на удаление этого кота")
    if request.method == 'POST':
        cat.delete()
        return redirect('cat_list')
    context = {'cat': cat}
    return render(request, 'cat/confirm_delete_cat.html', context)