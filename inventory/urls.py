from django.urls import path

from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    # Inventory views
    path('inventory/', views.list_items, name='inventory'),
    path('inventory/<int:id>', views.display_item, name='display_item'),
    path('inventory/delete/<int:id>', views.delete_item, name='delete_item'),

    # Recepes views
    path('menu/', views.list_menu, name='menu'),
    # path('recipes/<int:id>', views.display_recipe, name='display_item'),
    # path('recipes/delete/<int:id>', views.delete_recipe, name='delete_item'),


    # Purchase views
    path('purchase/', views.PurchaseView.as_view(), name='purchase'),

    # Report views
    path('report/', views.ReportView.as_view(), name='report'),
]
