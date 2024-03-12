from django.urls import path

from . import views

urlpatterns = [
    path('directors/', views.DirectorAPIView.as_view()),
    path('directors/<int:id>/', views.DirectorDetailAPIView.as_view()),
    path('movies/', views.MovieAPIView.as_view()),
    path('movies/<int:id>/', views.MovieDitailAPIView.as_view()),
    path('reviwes/', views.ReviewAPIView.as_view()),
    path('reviwes/<int:id>/', views.ReviewDitailAPIView.as_view()),
]