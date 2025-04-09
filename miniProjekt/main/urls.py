from django.urls import path
from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('create-order', views.OrderCreateView.as_view(), name='create_order')
]
