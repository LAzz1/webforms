from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('update/<str:pk>', views.update, name='update'),
    path('view/', views.view, name='view'),
    path('success/', views.thankyoupage, name='thankyoupage'),
    path('delete/<str:pk>', views.deleteItem, name='delete')
]

