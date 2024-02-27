from django.urls import path

from . import views

urlpatterns = [
    path('directors/', views.director_list),
    path('directors/<int:id>/', views.director_detail),
    path('movies/', views.movie_list),
    path('movies/<int:id>/', views.movie_detail),
    path('reviwes/', views.review_list),
    path('reviwes/<int:id>/', views.review_detail),
]