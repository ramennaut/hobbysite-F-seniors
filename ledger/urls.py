from django.urls import path
from . import views

urlpatterns = [
    path('recipes/list/', views.recipe_list, name='recipe_list'),
    path('recipe/1/', views.recipe_1, name='recipe_1'),
    path('recipe/2/', views.recipe_2, name='recipe_2'),
]
