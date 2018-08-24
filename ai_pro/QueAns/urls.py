from django.urls import path
from QueAns.views import index, ques, result, base, home, register, user_login


urlpatterns = [
    path('home', home, name='home'),
    path('base', base, name='base'),
    path('register', register, name='register'),
    path('login', user_login, name='user_login'),
    path('dataset', index, name='dataset'),
    path('form', ques, name='form'),
    path('result', result, name='result'),
]
