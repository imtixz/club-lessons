from django.urls import path
from .views import home, user_login, user_logout, register, beginner, novice, openV, advanced

urlpatterns = [
    path('', home, name='home'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('register/', register, name='register'),
    path('beginner/', beginner, name='beginner'),
    path('novice/', novice, name='novice'),
    path('open/', openV, name='open'),
    path('advanced/', advanced, name='advanced'),

]
