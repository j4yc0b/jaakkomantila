from django.urls import path
from . import views
from users import views as user_views

urlpatterns = [
    path('', views.projects, name="projects"),
    path('', user_views.navbar, name="navbar"),
    path('project/<str:pk>/', views.project, name="project"),
    
    # path('aboutme/', views.aboutme, name="aboutme"),
]

