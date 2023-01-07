from django.views.generic import ListView, TemplateView

from .models import Ingredient


class HomeView(TemplateView):
    template_name = 'inventory/home.html'


class InventoryView(ListView):
    template_name = 'inventory/inventory.html'
    model = Ingredient


class RecipesView(TemplateView):
    template_name = 'inventory/recipes.html'


class PurchaseView(TemplateView):
    template_name = 'inventory/purchase.html'


class ReportView(TemplateView):
    template_name = 'inventory/report.html'
