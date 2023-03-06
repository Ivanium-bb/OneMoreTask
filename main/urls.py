from django.urls import path

from main.views import FoodView

urlpatterns = [
    path('foods/', FoodView.as_view()),
]
