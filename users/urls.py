from django.urls import path
from users.views import RegisterUserView
from users import views

urlpatterns = [
    path('confirm/', views.ConfirmAPIView.as_view()),
    path('login/', views.LoginAPIView.as_view()),
    path('register/', RegisterUserView.as_view()),
]