from django import forms

class Feedbackform(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    
