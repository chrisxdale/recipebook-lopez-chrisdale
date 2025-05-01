from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Recipe, RecipeImage, RecipeIngredient, Ingredient
from .forms import RecipeForm, RecipeImageForm, RecipeIngredientForm, IngredientForm
from django.urls import reverse_lazy

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
    extra_context = {"images":RecipeImage.objects.all}

class RecipeCreateView(LoginRequiredMixin, CreateView):
    '''     
    @cn RecipeCreateView
    @brief Contains the form view for adding recipes
    '''
    model = Recipe
    template_name = "recipe_form.html"
    form_class = RecipeForm
    success_url = "/recipe/add/recipeingredient/"
 
    def form_valid(self, form):
        form.instance.author = self.request.user.profile
        return super().form_valid(form)
 
    def get_context_data(self, **kwargs):
        context = super(RecipeCreateView, self).get_context_data(**kwargs)
        context['recipe_form'] = context['form']
        return context

class RecipeIngredientCreateView(LoginRequiredMixin, CreateView):
    '''     
    @cn RecipeIngredientCreateView
    @brief Contains the form view for adding ingredient or recipe ingredient
    '''
    model = RecipeIngredient
    template_name = "recipeingredient_form.html"
    form_class = RecipeIngredientForm
    success_url = reverse_lazy('ledger:recipes-list')

    def get_context_data(self, **kwargs):
        context = super(RecipeIngredientCreateView, self).get_context_data(**kwargs)
        context['recipeingredient_form'] = context['form']
        return context

class IngredientCreateView(LoginRequiredMixin, CreateView):
    '''     
    @cn IngredientCreateView
    @brief Contains the form view for adding ingredient
    '''
    model = Ingredient
    template_name = "ingredient_form.html"
    form_class = IngredientForm
    success_url = "/recipe/add/recipeingredient/"

    def get_context_data(self, **kwargs):
        context = super(IngredientCreateView, self).get_context_data(**kwargs)
        context['ingredient_form'] = context['form']
        return context

class RecipeImageCreateView(LoginRequiredMixin, CreateView):
    '''     
    @cn RecipeImageCreateView
    @brief Contains the form view for adding recipe images
    '''
    model = RecipeImage
    template_name = "recipeimage_form.html"
    form_class = RecipeImageForm

    def get_success_url(self):
        return reverse_lazy('ledger:recipe-detail', kwargs={ 'pk': self.object.recipe.pk })

    def get_context_data(self, **kwargs):
        context = super(RecipeImageCreateView, self).get_context_data(**kwargs)
        context['recipeimage_form'] = context['form']
        return context
