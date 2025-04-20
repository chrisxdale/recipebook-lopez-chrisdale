from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Recipe

class RecipeListView(LoginRequiredMixin, ListView):
    '''     
    @cn RecipeListView
    @brief Contains the required given context for the RecipeList and
    renders the html page for the Recipe List
    '''
    context_object_name = 'recipes'
    queryset = Recipe.objects.all()
    template_name = 'recipes.html'

class RecipeDetailView(LoginRequiredMixin, DetailView):
    '''     
    @cn RecipeDetailView
    @brief Contains the context for the Recipe and
    renders the html page for the Recipe
    '''
    context_object_name = 'recipe'
    model = Recipe
    template_name = 'recipe.html'
