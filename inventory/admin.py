from django.contrib import admin

from .models import Ingredient


class IngridientsAdmin(admin.ModelAdmin):
    list_display = ('name', 'quantity', 'unit', 'price_unit')


admin.site.register(Ingredient, IngridientsAdmin)
