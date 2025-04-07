from django.shortcuts import render
from .models import Recipe

def index(request):
    return HttpResponse('Default Page')


def recipes_list(request):
    '''     
    @fn recipes_list
    @brief Contains the required given context for the recipes_list and
    renders the html page for the recipe_list
    '''
    recipes = Recipe.objects.all()
    return render(request, 'recipes.html', {'recipes': recipes})

def recipe_details(request, id):
    '''     
    @fn recipe_details
    @brief Contains the context for the recipes and
    renders the html page for the recipes
    '''
    recipe = Recipe.objects.get(id=id)
    ctx = {
        'recipe': recipe,
    }
    return render(request, 'recipe.html', ctx)
