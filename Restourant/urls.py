from django.urls import path
from .views import CreateDishView, DishListView, RulesListView, CreateRulesView

urlpatterns = [
    path('create_dish/', CreateDishView.as_view(), name='create_dish'),
    path('', DishListView.as_view(), name='dish_list'),
    path('rules/', RulesListView.as_view(), name='rules_list'),
    path('create_rule/', CreateRulesView.as_view(), name='create_rule'),
]
