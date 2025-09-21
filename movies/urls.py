
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('details',views.details, name='details'),
    path('<slug:slug>/', views.movie_detail, name='movie_detail'),
]