from django.urls import path
from .views.auth_view import login_view, register_view, logout_view
from .views.main_view import index_view, add_task

urlpatterns = [
    path('',index_view,name='index'),
    path('login/',login_view,name='login'),
    path('register/',register_view,name='register'),
    path('logout/',logout_view,name='logout'),
    path('add_task/',add_task,name='add_task')
]