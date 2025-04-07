from django.shortcuts import render
from .models import Recipe, RecipeIngredient

def index(request):
    return HttpResponse('Default Page')


def recipes_list(request):
    '''     
    @fn recipes_list
    @brief Contains the required given context for the recipes_list and
    renders the html page for the recipe_list
    '''
    recipes = Recipe.objects.all()
    return render(request, 'recipes_list.html', ctx)

def recipe_details(request), id:
    '''     
    @fn recipe_one
    @brief Contains the required given context for the recipe 1 and
    renders the html page for the recipe 1.
    '''
    recipe = Recipe.objects.get(id=id)
    recipe_ingredient = RecipeIngredient.objects.filter(Recipe = recipe)
    ctx = {
        'recipe': recipe,
        'recipe_ingredient': recipe_ingredient,
    }
    return render(request, 'recipe_two.html', ctx=)
