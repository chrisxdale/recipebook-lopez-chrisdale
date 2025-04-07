from django.db import models
from django.urls import reverse

class Ingredient(models.Model):
    '''     
    @fn Ingredient
    @brief The model class for Ingredient
    '''
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('ledger:recipe-details', args=[self.pk])

class Recipe(models.Model):
    '''     
    @fn Recipe
    @brief The model class for Recipe
    '''
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('ledger:recipe-details', args=[self.pk])

class RecipeIngredient(models.Model):
    '''     
    @fn RecipeIngredients
    @brief The model class for RecipeIngredient
    '''
    Quantity = models.CharField(max_length=100)
    Ingredient = models.ForeignKey(
        Ingredient,
        on_delete=models.CASCADE,
        related_name="recipe",
    )
    Recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        related_name="ingredients"
    )
