from django import forms
from django.contrib.auth.models import User

from QueAns.models import Cos_Sim, Review

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')


class Ques(forms.Form):
    pass_result = forms.IntegerField(help_text='Please rate the pass percentage between 5 to 9')
    extra_curriculum = forms.IntegerField(help_text='Enter 1 to consider "Yes" 0 to consider "No".')
    expensive = forms.IntegerField(help_text='Enter 1 to consider "Yes" 0 to consider "No".')
    dress = forms.IntegerField(help_text='Enter 1 to consider "Yes" 0 to consider "No".')
    strict = forms.IntegerField(help_text='Enter 1 to consider "Yes" 0 to consider "No".')
    science = forms.IntegerField(help_text='Enter 1 to consider "Yes" 0 to consider "No".')
    management = forms.IntegerField(help_text='Enter 1 to consider "Yes" 0 to consider "No".')


class Variable(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['variable']
