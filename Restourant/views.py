from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.views import View
from .models import Dish, DishType, Cooker, Rules
from .forms import DishForm, RuleForm

class CreateDishView(View):
    def get(self, request):
        form = DishForm()
        return render(request, 'create_dish.html', {'form': form})

    def post(self, request):
        form = DishForm(request.POST)
        if form.is_valid():
            dish = form.save()
            return redirect('dish_list')
        return render(request, 'create_dish.html', {'form': form})

class DishListView(View):
    def get(self, request):
        dishes = Dish.objects.all()
        return render(request, 'dish_list.html', {'dishes': dishes})

class RulesListView(View):
    def get(self, request):
        rules = Rules.objects.all()
        return render(request, 'rules.html', {'rules': rules})

class CreateRulesView(View):
    def get(self, request):
        form = RuleForm()
        return render(request, 'create_rules.html', {'form': form})

    def post(self, request):
        form = RuleForm(request.POST)
        if form.is_valid():
            rule = form.save()
            return redirect('rules_list')
        return render(request, 'create_rules.html', {'form': form})
