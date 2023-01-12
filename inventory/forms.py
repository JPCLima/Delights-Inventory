from django import forms

from .models import Ingredient, MenuItem


class EditForm(forms.ModelForm):
    class Meta:
        model = Ingredient
        fields = ("name", "quantity", "unit", "price_unit")


class MenuForm(forms.ModelForm):
    class Meta(object):
        model = MenuItem
        fields = ("title", "price")
