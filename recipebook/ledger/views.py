from django.shortcuts import render

def index(request):
    return HttpResponse('Default Page')


def recipes_list(request):
    '''     
    @fn recipes_list
    @brief Contains the required given context for the recipes_list and
    renders the html page for the recipe_list
    '''
    ctx = {
            "recipes": [
                {
                    "name": "Recipe 1",
                    "ingredients": [
                        {
                            "name": "tomato",
                            "quantity": "3pcs"
                        },
                        {
                            "name": "onion",
                            "quantity": "1pc"
                        },
                        {
                            "name": "pork",
                            "quantity": "1kg"
                        },
                        {
                            "name": "water",
                            "quantity": "1L"
                        },
                        {
                            "name": "sinigang mix",
                            "quantity": "1 packet"
                        }
                    ],
                    "link": "/recipe/1"
                },
                {
                    "name": "Recipe 2",
                    "ingredients": [
                        {
                            "name": "garlic",
                            "quantity": "1 head"
                        },
                        {
                            "name": "onion",
                            "quantity": "1pc"
                        },
                        {
                            "name": "vinegar",
                            "quantity": "1/2cup"
                        },
                        {
                            "name": "water",
                            "quanity": "1 cup"
                        },
                        {
                            "name": "salt",
                            "quantity": "1 tablespoon"
                        },
                        {
                            "name": "whole black peppers",
                            "quantity": "1 tablespoon"
                        },
                        {
                            "name": "pork",
                            "quantity": "1 kilo"
                        }
                    ],
                    "link": "/recipe/2"
                }
            ]
        }
    return render(request, 'recipes_list.html', ctx)

def recipe_one(request):
    '''     
    @fn recipe_one
    @brief Contains the required given context for the recipe 1 and
    renders the html page for the recipe 1.
    '''
    ctx = {
            "name": "Recipe 1",
            "ingredients": [
                {
                    "name": "tomato",
                    "quantity": "3pcs"
                },
                {
                    "name": "onion",
                    "quantity": "1pc"
                },
                {
                    "name": "pork",
                    "quantity": "1kg"
                },
                {
                    "name": "water",
                    "quantity": "1L"
                },
                {
                    "name": "sinigang mix",
                    "quantity": "1 packet"
                }
            ],
            "link": "/recipe/1"
        }
    return render(request, 'recipe_one.html', ctx)

def recipe_two(request):
    '''     
    @fn recipe_two
    @brief Contains the required given context for the recipe 2 and
    renders the html page for the recipe 2.
    '''
    ctx = {
            "name": "Recipe 2",
            "ingredients": [
                {
                    "name": "garlic",
                    "quantity": "1 head"
                },
                {
                    "name": "onion",
                    "quantity": "1pc"
                },
                {
                    "name": "vinegar",
                    "quantity": "1/2cup"
                },
                {
                    "name": "water",
                    "quantity": "1 cup"
                },
                {
                    "name": "salt",
                    "quantity": "1 tablespoon"
                },
                {
                    "name": "whole black peppers",
                    "quantity": "1 tablespoon"
                },
                {
                    "name": "pork",
                    "quantity": "1 kilo"
                }
            ],
            "link": "/recipe/2"
        }
    return render(request, 'recipe_two.html', ctx)
