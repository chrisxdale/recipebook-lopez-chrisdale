from django.urls import path
from . import views

urlpatterns = [
    path('recipes/list', views.recipes_list, name='recipes-list'),
    path('recipe/<int:id>', views.recipe_details, name='recipe-details'),
]

APP_NAME = "ledger"
