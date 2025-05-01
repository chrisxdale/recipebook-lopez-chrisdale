from django import forms
from .models import Recipe, RecipeImage, RecipeIngredient, Ingredient
 
class RecipeForm(forms.ModelForm):
    '''
    @cn RecipeForm
    @brief The form model form for RecipeForm
    '''
    class Meta:
        model = Recipe
        fields = ["name"]
 
class RecipeIngredientForm(forms.ModelForm):
    '''
    @cn RecipeIngredientForm
    @brief TThe form model form for RecipeIngredientForm
    '''
    class Meta:
        model = RecipeIngredient
        fields = ["Recipe", "Ingredient", "Quantity"]
 
class IngredientForm(forms.ModelForm):
    '''
    @cn IngredientForm
    @brief The form model form for IngredientForm
    '''
    class Meta:
        model = Ingredient
        fields = "__all__"
 
class RecipeImageForm(forms.ModelForm):
    '''
    @cn RecipeImageForm
    @brief The form model form for RecipeImageForm
    '''
    class Meta:
        model = RecipeImage
        fields = "__all__"