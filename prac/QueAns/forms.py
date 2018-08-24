from django import forms
from django.contrib.auth.models import User

from QueAns.models import Cos_Sim, Review

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')


class Ques(forms.Form):
    pass_result = forms.IntegerField(min_value=3, max_value=9, help_text='Please rate the pass percentage between 3 to 9',error_messages={'required': 'Please enter your name'})
    extra_curriculum = forms.IntegerField(min_value=0, max_value=1, help_text='Enter 1 to consider "Yes" 0 to consider "No".')
    expensive = forms.IntegerField(min_value=3, max_value=9, help_text='Please rate the pass percentage between 3 to 9')
    dress = forms.IntegerField(min_value=0, max_value=1, help_text='Enter 1 to consider "Yes" 0 to consider "No".')
    strict = forms.IntegerField(min_value=0, max_value=1, help_text='Enter 1 to consider "Yes" 0 to consider "No".')
    science = forms.IntegerField(min_value=0, max_value=1, help_text='Enter 1 to consider "Yes" 0 to consider "No".')
    management = forms.IntegerField(min_value=0, max_value=1, help_text='Enter 1 to consider "Yes" 0 to consider "No".')


class Variable(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['variable']
