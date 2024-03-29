from django.urls import path, include
from .views import dish_list, create_dish
from Restourant import views


urlpatterns = [
    path('create_dish/', create_dish, name='create_dish'),
    path('', views.dish_list, name='dish_list'),
    path('rules/', views.rules_list, name='rules_list'),
    path('create_rule/', views.create_rules, name='create_rule'),
]