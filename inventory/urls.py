from django.urls import path

from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    # Inventory views
    path('inventory/',
         views.InventoryView.as_view(), name='inventory'),
    path('inventory/<int:id>',
         views.InventoryView.as_view(), name='inventory'),
    path('/inventory/<int:id>/delete/',
         views.InventoryView.as_view(), name='delete_inventory'),


    # Recepes views
    path('recipes/', views.RecipesView.as_view(), name='recipes'),

    # Purchase views
    path('purchase/', views.PurchaseView.as_view(), name='purchase'),

    # Report views
    path('report/', views.ReportView.as_view(), name='report'),
]
