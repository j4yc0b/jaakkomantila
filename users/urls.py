from django.urls import path
from . import views

urlpatterns = [
    path('', views.profiles, name="profiles"),
    path('profiles/<str:pk>/', views.user_profile, name="user_profile"),
    path('aboutme/', views.aboutme, name="aboutme"),
    path('aboutme/', views.skills, name="skills"),
]
