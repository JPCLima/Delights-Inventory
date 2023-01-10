from django import forms

from .models import Ingredient


class EditForm(forms.ModelForm):
    class Meta:
        model = Ingredient
        fields = ("name", "quantity", "unit", "price_unit")
