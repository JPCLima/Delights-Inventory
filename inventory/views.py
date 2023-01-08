from django.shortcuts import redirect, render
from django.views import View
from django.views.generic import TemplateView

from .forms import IngredientForm
from .models import Ingredient


class HomeView(TemplateView):
    template_name = 'inventory/home.html'


class InventoryView(View):
    template_name = 'inventory/inventory.html'
    model = Ingredient
    form_class = IngredientForm

    http_method_names = ['get', 'post', 'delete']

    def get(self, request, id=None):
        if id:
            obj = self.model.objects.get(pk=id)
            form = self.form_class(instance=obj)
        else:
            form = self.form_class()

        object_list = self.model.objects.all()
        context = {'object_list': object_list, 'form': form}
        return render(request, self.template_name, context)

    def post(self, request, id=None):
        if id:
            obj = self.model.objects.get(pk=id)
            form = self.form_class(request.POST, instance=obj)
        else:
            form = self.form_class(request.POST)

        if form.is_valid():
            form.save()
            return redirect('inventory')
        else:
            object_list = self.model.objects.all()
            context = {'object_list': object_list, 'form': form}
            return render(request, self.template_name, context)

    def delete(self, request, id):
        print('delete')
        obj = self.model.objects.get(pk=id)
        obj.delete()
        return redirect('inventory')


class RecipesView(TemplateView):
    template_name = 'inventory/recipes.html'


class PurchaseView(TemplateView):
    template_name = 'inventory/purchase.html'


class ReportView(TemplateView):
    template_name = 'inventory/report.html'
