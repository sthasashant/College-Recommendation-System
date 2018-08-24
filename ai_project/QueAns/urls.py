from django.urls import path
from QueAns.views import index, ques, result


urlpatterns = [
    path('dataset', index, name='dataset'),
    path('form', ques, name='form'),
    path('result', result, name='result'),
]
