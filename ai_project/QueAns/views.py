from django.shortcuts import render, redirect
from django.db.models import F
from django.views.generic import DetailView
from QueAns.models import College, Review, Cos_Sim
from QueAns import forms
import math
# Create your views here.


def index(request):
    dataset = Review.objects.all()

    dd = list(dataset)

    return render(request, 'dataset.html', {'data': dataset, 'ddd':dd} )


def ques(request):
    form = forms.Ques()
    result = []
    coll_name = []

    if request.method == 'POST':
        form = forms.Ques(request.POST)


        if form.is_valid():

            form.save()

    return render(request, 'quens.html', {'form': form})


def result(request):

    return render(request, 'result.html')
