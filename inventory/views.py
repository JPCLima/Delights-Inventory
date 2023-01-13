from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import TemplateView

from .forms import EditForm, MenuForm, PurchaseForm
from .models import Ingredient, MenuItem, Purchase


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


def display_menu(request, id):
    """List menus on the table"""
    menu = get_object_or_404(MenuItem, pk=id)
    if request.method == 'POST':
        form = MenuForm(request.POST, instance=menu)
        if form.is_valid():
            form.save()
            return redirect('menu')

    else:
        editform = MenuForm(instance=menu)
        menus = MenuItem.objects.all()
        context = {'menus': menus,
                   'formEdit': editform}
        return render(request, 'menu/menu.html', context)


def delete_menu(request, id):
    """Delete the selected item from the inventory"""
    menu = get_object_or_404(MenuItem, pk=id)
    menu.delete()
    return redirect('menu')


# PURCHASE VIEW
def list_purchase(request):
    """ List the menu """
    if request.method == 'POST':
        form = PurchaseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('purchase')
    else:
        purchases = Purchase.objects.all()
        context = {'purchases': purchases,
                   'formEdit': PurchaseForm}
        return render(request, 'purchase/purchase.html', context)


def display_purchase(request, id):
    """List menus on the table"""
    purchase = get_object_or_404(Purchase, pk=id)
    if request.method == 'POST':
        form = PurchaseForm(request.POST, instance=purchase)
        if form.is_valid():
            form.save()
            return redirect('purchase')

    else:
        editform = PurchaseForm(instance=purchase)
        purchases = Purchase.objects.all()
        context = {'purchases': purchases,
                   'formEdit': editform}
        return render(request, 'purchase/purchase.html', context)


def delete_purchase(request, id):
    """Delete the selected item from the inventory"""
    purchase = get_object_or_404(Purchase, pk=id)
    purchase.delete()
    return redirect('purchase')


class ReportView(TemplateView):
    template_name = 'inventory/report.html'
