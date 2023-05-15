from django import forms

class Feedbackform(forms.Form):
    name = forms.CharField(required=True,)
    raiting = forms.IntegerField(min_value=1, max_value=5 )
    text = forms.CharField(label="Your Feedback",widget=forms.Textarea,max_length=200)
    
