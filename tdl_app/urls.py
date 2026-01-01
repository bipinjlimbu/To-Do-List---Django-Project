from django.urls import path
from .views.auth_view import login_view, register_view
from .views.main_view import index_view

urlpatterns = [
    path('',index_view,name='index'),
    path('login/',login_view,name='login'),
    path('register/',register_view,name='register'),
]