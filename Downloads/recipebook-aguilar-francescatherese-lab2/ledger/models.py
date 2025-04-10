from django.db import models
from django.urls import reverse


class Recipe(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("recipe_detail", args=[str(self.pk)])


class Ingredient(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class RecipeIngredient(models.Model):
    quantity = models.CharField(max_length=100)
    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        null=True,
        related_name="ingredients"
    )
    ingredient = models.ForeignKey(
        Ingredient,
        on_delete=models.CASCADE,
        null=True,
        related_name="recipe"
    )

    def __str__(self):
        return f"{self.quantity} {self.ingredient.name} for {self.recipe.name}"
