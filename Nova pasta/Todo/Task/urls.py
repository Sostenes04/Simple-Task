from django.urls import path

from . import views 


urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('Task/<int:pk>/', views.Detalhe.as_view(), name='detalhe'),
]