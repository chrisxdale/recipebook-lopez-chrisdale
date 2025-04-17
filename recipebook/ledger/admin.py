from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from .models import Ingredient, Recipe, RecipeIngredient, Profile

class IngredientAdmin(admin.ModelAdmin):
    '''     
    @cn IngredientAdmin
    @brief The admin class for Ingredient
    '''
    model = Ingredient

    list_display = ('name',)

class RecipeAdmin(admin.ModelAdmin):
    '''     
    @cn RecipeAdmin
    @brief The admin class for Recipe
    '''
    model = Recipe

    list_display = ('name',)

class RecipeIngredientAdmin(admin.ModelAdmin):
    '''     
    @cn RecipeIngredientAdmin
    @brief The admin class for RecipeIngredient
    '''
    model = RecipeIngredient

    list_display = ('Quantity', 'Ingredient', 'Recipe',)

class ProfileInline(admin.StackedInline):
    '''     
    @cn ProfileInline
    @brief Contains the Profile Model which to be used in UserAdmin
    '''
    model = Profile
    can_delete = False

class UserAdmin(admin.BaseUserAdmin):
    '''     
    @cn UserAdmin
    @brief The admin class for User
    '''
    inlines = [ProfileInline,]

admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(Ingredient, IngredientAdmin)
admin.site.register(Recipe, RecipeAdmin)
admin.site.register(RecipeIngredient, RecipeIngredientAdmin)
