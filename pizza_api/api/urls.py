from django.urls import path
from . import views

urlpatterns = [
    path('', views.menu_list,name="menu_list"),
    path('<int:id>/', views.menu_chosen,name="menu_chosen"),
]