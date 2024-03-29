from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from .models import Dish, DishType, Cooker, Rules
from .forms import DishForm, RuleForm

def create_dish(request):
    if request.method == 'POST':
        form = DishForm(request.POST)
        if form.is_valid():
            dish = form.save()
            return redirect('dish_list')
    else:
        form = DishForm()

    return render(request, 'create_dish.html', {'form': form})

def dish_list(request):
    dishes = Dish.objects.all()
    return render(request, 'dish_list.html', {'dishes': dishes})

def rules_list(request):
    rules = Rules.objects.all()
    return render(request, 'rules.html', {'rules': rules})

def create_rules(request):
    if request.method == 'POST':
        form = RuleForm(request.POST)
        if form.is_valid():
            rule = form.save()
            return redirect('rules_list')
    else:
        form = RuleForm()

    return render(request, 'create_rules.html', {'form': form})