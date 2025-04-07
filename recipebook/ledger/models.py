from django.db import models

class Ingredient(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('ingredient_detail', arg=[str(self.name)])

class Recipe(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
         return self.name
     
    def get_absolute_url(self):
         return reverse('recipesInDatabase')

class RecipeIngredient(models.Model):
    Quantity = models.CharField(max_length=100)
    Ingredient = models.ForeignKey(
        Ingredient,
        on_delete=models.CASCADE,
    )
    Recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
    )
