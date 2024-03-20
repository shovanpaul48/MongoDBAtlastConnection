from django.urls import path
from . import views

urlpatterns = [
    path('', views.form_view, name='form'),
    path('success/', views.success_view, name='success'),
    path('view/', views.view_data, name='view_data'),
]
