from .import views
from django.urls import path

urlpatterns = [
    path("",views.home,name="home"),
    path('login/', views.login_page, name="login"),
    path('users/', views.users_page, name="users"),
    path('register/', views.register_page, name="register"),
]