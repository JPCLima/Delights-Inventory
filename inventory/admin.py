from django.contrib import admin

from .models import Ingredient, MenuItem, Purchase, RecipeManager


class IngridientsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'quantity', 'unit', 'price_unit')


class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'price')


class RecipeManagerAdmin(admin.ModelAdmin):
    """ list_display = ('menu_items', 'ingredient', 'quantity') """
    list_display = ("menu_items", "get_ingredients", "quantity")

    def get_ingredients(self, obj):
        return [ingredient.name for ingredient in obj.ingredient.all()]


class PurchaseAdmin(admin.ModelAdmin):
    list_display = ('menu_item', 'timestamp')


admin.site.register(Ingredient, IngridientsAdmin)
admin.site.register(MenuItem, MenuItemAdmin)
admin.site.register(Purchase, PurchaseAdmin)
admin.site.register(RecipeManager, RecipeManagerAdmin)
