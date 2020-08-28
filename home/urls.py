from . import views
from django.urls import path

urlpatterns = [
    path('', views.Home, name="Home"),
    path('add/', views.Add, name="add"),
    path('post/<str:slug>', views.View, name="viewPost"),
    path('update/<id>', views.Update, name="UpdatePost"),
    path('delete/<id>', views.Delete,name="DeletePost"),
    path('login/',views.Login,name="LoginPage"),
    path('register/',views.Register,name="RegisterPage"),
]