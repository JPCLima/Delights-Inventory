from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import TemplateView

from .forms import EditForm, MenuForm
from .models import Ingredient, MenuItem


class HomeView(TemplateView):
    template_name = 'inventory/home.html'


# INVENTORY VIEW
def list_items(request):
    """List items on the table"""
    if request.method == 'POST':
        form = EditForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('inventory')
    else:
        items = Ingredient.objects.all()
        context = {'ingredients': items,
                   'formEdit': EditForm}
        return render(request, 'inventory/inventory.html', context)


def display_item(request, id):
    """List items on the table"""
    ingredient = get_object_or_404(Ingredient, pk=id)
    if request.method == 'POST':
        form = EditForm(request.POST, instance=ingredient)
        if form.is_valid():
            form.save()
            return redirect('inventory')

    else:
        editform = EditForm(instance=ingredient)
        items = Ingredient.objects.all()
        context = {'ingredients': items,
                   'formEdit': editform}
        return render(request, 'inventory/inventory.html', context)


def delete_item(request, id):
    """Delete the selected item from the inventory"""
    ingredient = get_object_or_404(Ingredient, pk=id)
    ingredient.delete()
    return redirect('inventory')


# RECIPES VIEW
def list_menu(request):
    """ List the menu """
    if request.method == 'POST':
        form = MenuForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('menu')
    else:
        menus = MenuItem.objects.all()
        context = {'menus': menus,
                   'formEdit': MenuForm}
        return render(request, 'menu/menu.html', context)


""" class RecipesView(TemplateView):
    template_name = 'recipes/recipes.html'

 """


class PurchaseView(TemplateView):
    template_name = 'inventory/purchase.html'


class ReportView(TemplateView):
    template_name = 'inventory/report.html'
