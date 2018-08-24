from django.shortcuts import render, redirect
from django.db.models import F
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from django.views.generic import DetailView
from QueAns.models import College, Review, Cos_Sim
from QueAns import forms
import math
# Create your views here.


def index(request):
    dataset = Review.objects.all()

    dd = list(dataset)

    return render(request, 'dataset.html', {'data': dataset, 'ddd':dd} )

def about(request):
    return render(request, 'about.html')

def home(request):
    return render(request, 'home.html')

def base(request):
    return render(request, 'base.html')


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))

def register(request):

    registered = False

    if request.method == 'POST':
        user_form = forms.UserForm(data = request.POST)

        if user_form.is_valid():

            user = user_form.save()
            user.set_password(user.password)
            user.save()

            registered = True
        else:
            print(user_form.errors)

    else:
        user_form = forms.UserForm()

    return render(request, 'registration.html',
                            {'user_form': user_form,
                            'registered': registered})


def user_login(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('home'))

            else:
                return HttpResponse("Account is not active")
        else:
            return HttpResponse("Your Username and password is incoorect")
    else:
        return render(request, 'login.html',{})



@login_required
def ques(request):
    form = forms.Ques()

    if request.method == 'POST':
        form = forms.Ques(request.POST)


        if form.is_valid():

            for x in range(20):
                data = Review.objects.all()[x]


                vecta_vectb = (data.pass_result*form.cleaned_data['pass_result']+
                                data.extra_curriculum*form.cleaned_data['extra_curriculum']+
                                data.expensive*form.cleaned_data['expensive']+
                                data.dress*form.cleaned_data['dress']+
                                data.strict*form.cleaned_data['strict']+
                                data.science*form.cleaned_data['science']+
                                data.management*form.cleaned_data['management']
                            )

                mod_a = math.sqrt(
                            data.pass_result*data.pass_result+
                            data.extra_curriculum*data.extra_curriculum+
                            data.expensive*data.expensive+
                            data.dress*data.dress+
                            data.strict*data.strict+
                            data.science*data.science+
                            data.management*data.management
                            )

                mod_b = math.sqrt(
                            form.cleaned_data['pass_result']*form.cleaned_data['pass_result']+
                            form.cleaned_data['extra_curriculum']*form.cleaned_data['extra_curriculum']+
                            form.cleaned_data['expensive']*form.cleaned_data['expensive']+
                            form.cleaned_data['dress']*form.cleaned_data['dress']+
                            form.cleaned_data['strict']*form.cleaned_data['strict']+
                            form.cleaned_data['science']*form.cleaned_data['science']+
                            form.cleaned_data['management']*form.cleaned_data['management']
                )

                cosine_sim = vecta_vectb/(mod_a*mod_b)
                data.variable = cosine_sim
                data.save()

            return redirect('result')
    return render(request, 'quens.html', {'form': form})


def result(request):
    coll_name = []

    for x in range(20):
        simi = Review.objects.all()[x]

        if simi.variable >= 0.98:
            coll_name.append(simi.college.name)


    return render(request, 'result.html', {'college': coll_name})
