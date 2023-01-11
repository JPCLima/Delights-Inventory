from django.db import models


class Ingredient(models.Model):
    """Represents a single Ingredient"""
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=100, unique=True)
    quantity = models.FloatField(default=0)
    unit = models.CharField(max_length=100)
    price_unit = models.FloatField(default=0.00)

    def get_absolute_url(self):
        return "/ingredients"

    def __str__(self):
        return f"""
        name: {self.name};
        quantity: {self.quantity};
        unit: {self.unit};
        price_unit: {self.price_unit}
        """


class MenuItem(models.Model):
    """Menu Item represents a entry menu in the restaurant"""
    title = models.CharField(max_length=200, unique=True)
    price = models.FloatField(default=0.00)

    def get_absolute_url(self):
        return "/menu"

    def __str__(self):
        return f"""{self.title} | {self.price}"""


class RecipeManager(models.Model):
    """Represents a ingredients needed for a recipe"""
    menu_items = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    ingredient = models.ManyToManyField(Ingredient)
    quantity = models.FloatField(default=0.0)

    def get_absolute_url(self):
        return "/menu"

    def __str__(self):
        return f"""{self.menu_items} | {self.quantity}"""


class Purchase(models.Model):
    """Represent the purchase of the menu"""
    menu_item = models.ForeignKey(RecipeManager, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_created=True)

    def get_absolute_url(self):
        return "/purchases"

    def save(self, *args, **kwargs):
        self.menu_item.quantity -= 1
        if self.menu_item.quantity > 1:
            self.menu_item.save()
            super().save(*args, **kwargs)
        else:
            return False

    def __str__(self):
        return f"""{self.menu_item} | {self.timestamp}"""
