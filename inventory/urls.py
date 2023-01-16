from django.contrib.auth.decorators import login_required
from django.urls import path

from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    # Inventory views
    path('inventory/', views.list_items, name='inventory'),
    path('inventory/<int:id>', views.display_item, name='display_item'),
    path('inventory/delete/<int:id>', views.delete_item, name='delete_item'),

    # Menu views
    path('menu/', views.list_menu, name='menu'),
    path('menu/<int:id>', views.display_menu, name='display_menu'),
    path('menu/delete/<int:id>', views.delete_menu, name='delete_menu'),


    # Purchase views
    path('purchase/', views.list_purchase, name='purchase'),
    path('purchase/<int:id>', views.display_purchase, name='display_purchase'),
    path('purchase/delete/<int:id>', views.delete_purchase, name='delete_purchase'),

    # Report views
    path('report/', views.ReportView.as_view(), name='report'),
]
