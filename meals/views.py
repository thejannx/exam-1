from django.shortcuts import render
from .models import Meal

def task_list(request):

    meal_name = request.GET.get('meal_name')
    ingredients = request.GET.get('ingredients')
    price = request.GET.get('price')
    type = request.GET.get('type')
    cuisine = request.GET.get('cuisine')


    if meal_name and ingredients and price and type and cuisine:
        Meal.objects.create(
            meal_name=meal_name,
            ingredients=ingredients,
            price=price,
            type=type,
            cuisine=cuisine
        )


    meals = Meal.objects.all()


    ctx = {'meals': meals}


    return render(request, 'meals/task_list.html', ctx)
