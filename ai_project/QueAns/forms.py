from django import forms

class Ques(forms.Form):
    pass_result = forms.IntegerField()
    extra_curriculum = forms.IntegerField()
    expensive = forms.IntegerField()
    dress = forms.IntegerField()
    strict = forms.IntegerField()
    science = forms.IntegerField()
    management = forms.IntegerField()
