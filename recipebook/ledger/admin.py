from django.contrib import admin
from .models import Ingredient, Recipe, RecipeIngredient

class IngredientAdmin(admin.ModelAdmin):
    '''     
    @fn IngredientAdmin
    @brief The admin class for Ingredient
    '''
    model = Ingredient

    list_display = ('name',)

class RecipeAdmin(admin.ModelAdmin):
    '''     
    @fn RecipeAdmin
    @brief The admin class for Recipe
    '''
    model = Recipe

    list_display = ('name',)

class RecipeIngredientAdmin(admin.ModelAdmin):
    '''     
    @fn RecipeIngredientAdmin
    @brief The admin class for RecipeIngredient
    '''
    model = RecipeIngredient

    list_display = ('Quantity', 'Ingredient', 'Recipe',)

admin.site.register(Ingredient, IngredientAdmin)
admin.site.register(Recipe, RecipeAdmin)
admin.site.register(RecipeIngredient, RecipeIngredientAdmin)
