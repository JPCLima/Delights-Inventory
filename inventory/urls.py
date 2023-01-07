from django.urls import path

from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('recipes/', views.RecipesView.as_view(), name='recipes'),
    path('inventory/', views.InventoryView.as_view(), name='inventory'),
    path('purchase/', views.PurchaseView.as_view(), name='purchase'),
    path('report/', views.ReportView.as_view(), name='report'),
]
