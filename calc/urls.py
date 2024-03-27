from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add', views.addNumbers, name='add'),
    path('view', views.viewUsers, name='view')
]
