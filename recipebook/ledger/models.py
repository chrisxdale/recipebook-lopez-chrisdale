from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    bio = models.CharField(max_length=255)

    def __str__(self):
        return self.name

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
    author = models.ForeignKey(
        Profile,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )
    created_on = models.DateTimeField(auto_now_add=True),
    updated_on = models.DateTimeField(auto_now=True),

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
