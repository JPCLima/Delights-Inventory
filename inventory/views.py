from django.shortcuts import get_object_or_404, redirect, render
from django.views import View
from django.views.generic import TemplateView

from .forms import EditForm
from .models import Ingredient


class HomeView(TemplateView):
    template_name = 'inventory/home.html'


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


"""
class InventoryView(View):
    template_name = 'inventory/inventory.html'
    model = Ingredient
    form_class = EditForm
    second_form_class = DeleteForm
    model = Ingredient

    http_method_names = ['get', 'post', 'delete']

    def get(self, request, id=None):
        if id:
            obj = self.model.objects.get(pk=id)
            form = self.form_class(instance=obj)
        else:
            form = self.form_class()

        ingredients = self.model.objects.all()
        context = {'ingredients': ingredients,
                   'form': form}
        return render(request, self.template_name, context)

    def post(self, request, id=None):

        if id:
            obj = self.model.objects.get(pk=id)
            form = self.form_class(request.POST, instance=obj)
            print("id")
            print(request.POST)
        else:
            if 'quantity' in request.POST:
                form = self.form_class(request.POST)
            else:
                form = self.second_form_class(request.POST)
                print(request.POST)

        if form.is_valid():
            if 'quantity' in request.POST:
                form.save()
                return redirect('inventory')
            else:
                print(request.POST)
                 obj = self.model.objects.get(pk=id)
                obj.delete() 
                return redirect('inventory')

        else:
            if 'quantity' in request.POST:
                object_list = self.model.objects.all()
                context = {'object_list': object_list, 'formDel': form}
                return render(request, self.template_name, context)
            else:
                print(request.POST)
                return redirect('inventory')
"""


class RecipesView(TemplateView):
    template_name = 'inventory/recipes.html'


class PurchaseView(TemplateView):
    template_name = 'inventory/purchase.html'


class ReportView(TemplateView):
    template_name = 'inventory/report.html'
