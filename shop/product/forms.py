from django import forms
from .models import Feedback
'''
class Feedbackform(forms.Form):
    name = forms.CharField(required=True,)
    rating = forms.IntegerField(min_value=1, max_value=5 )
    text = forms.CharField(label="Your Feedback",widget=forms.Textarea,max_length=200)
'''
class Feedbackform(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ["name","rating","text"]
        label = {"name":"Full Name"}