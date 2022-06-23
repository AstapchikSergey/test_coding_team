from django.urls import path

from foods.api.v1 import views

urlpatterns = [
    path('foods/', views.FoodsListApi.as_view()),
    path('food_categories/', views.FoodCategoryListApi.as_view()),
]
