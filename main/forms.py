from django import forms


class RequestForm(forms.Form):
    job = forms.CharField(max_length=100)
    school = forms.CharField(max_length=100)
    gender = forms.CharField(max_length=100)
