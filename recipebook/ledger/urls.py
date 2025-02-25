from django.urls import path
from .views import index, recipes_list, recipe_one, recipe_two

urlpatterns = [
    path('', index, name='index'),
    path('recipes/list', recipes_list, name='recipes-list'),
    path('recipes/1', recipe_one, name='recipe-one'),
    path('recipes/2', recipe_two, name='recipe-two'),
]

app_name = "ledger"