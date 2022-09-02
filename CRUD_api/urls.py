from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.add_items, name='add-items'),
    path('all/', views.view_items, name='view-items'),
    path('update/<int:pk>/', views.update_items, name='update-items')
]