from django import forms

class ContactForm(forms.Form):
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)
    email = forms.CharField(max_length=200)
    subject = forms.EmailField(max_length=150)
    message = forms.CharField(widget=forms.Textarea, max_length=2000)







