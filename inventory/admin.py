from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin

from .models import Ingredient, MenuItem, Purchase, RecipeManager


class IngredientResource(resources.ModelResource):
    class Meta:
        model = Ingredient


class MenuItemResource(resources.ModelResource):
    class Meta:
        model = MenuItem


class RecipeManagerResource(resources.ModelResource):
    class Meta:
        model = RecipeManager


class IngridientsAdmin(ImportExportModelAdmin):
    list_display = ('id', 'name', 'quantity', 'unit', 'price_unit')
    resource_class = IngredientResource


class MenuItemAdmin(ImportExportModelAdmin):
    list_display = ('id', 'title', 'price')
    resource_class = MenuItemResource


class RecipeManagerAdmin(ImportExportModelAdmin):
    list_display = ("menu_items", "get_ingredients", "quantity")
    resource_class = RecipeManagerResource

    def get_ingredients(self, obj):
        return [ingredient.name for ingredient in obj.ingredient.all()]


class PurchaseAdmin(admin.ModelAdmin):
    list_display = ('menu_item', 'timestamp')


admin.site.register(Ingredient, IngridientsAdmin)
admin.site.register(MenuItem, MenuItemAdmin)
admin.site.register(Purchase, PurchaseAdmin)
admin.site.register(RecipeManager, RecipeManagerAdmin)
