from django.urls import path
from catches import views

urlpatterns = [
    path('catches/', views.CatchList.as_view()),
    path('catches/<int:pk>/', views.CatchDetail.as_view()),
]