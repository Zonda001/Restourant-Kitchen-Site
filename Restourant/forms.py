from django import forms
from .models import Dish, Rules

class DishForm(forms.ModelForm):
    class Meta:
        model = Dish
        fields = ["name", "description", "price", "dish_type", "cooks"]

class RuleForm(forms.ModelForm):
    class Meta:
        model = Rules
        fields = ["name", "description"]