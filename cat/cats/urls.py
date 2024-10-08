from django.urls import path
from . import views

urlpatterns = [
    path('', views.cat_list, name='cat_list'),
    path('/create/', views.create_cat, name='create_cat'),
    path('/<int:pk>/edit/', views.edit_cat, name='edit_cat'),
    path('/<int:pk>/delete/', views.delete_cat, name='delete_cat'),
]