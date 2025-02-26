from django.urls import path
from .views import index, recipes_list, recipe_one, recipe_two

urlpatterns = [
    path('', index, name='index'),
    path('recipes/list', recipes_list, name='recipes-list'),
    path('recipe/1', recipe_one, name='recipe-one'),
    path('recipe/2', recipe_two, name='recipe-two'),
]

APP_NAME = "ledger"
