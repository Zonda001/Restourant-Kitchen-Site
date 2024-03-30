from django import forms
from .models import Dish, Rule

class DishForm(forms.ModelForm):
    class Meta:
        model = Dish
        fields = ["name", "description", "price", "dish_type", "cooks"]

class RuleForm(forms.ModelForm):
    class Meta:
        model = Rule
        fields = ["name", "description"]