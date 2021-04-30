from django.urls import path
from . import views
urlpatterns = [
    path('home', views.home),
    path('login/',views.login),
    path('register/', views.register),
    path('todo/', views.todo),
    path('save/',views.save),
    path('delete',views.delete),
    path('logout/',views.logout),
    
]