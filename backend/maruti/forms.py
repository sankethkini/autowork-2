from django import forms
from django.forms.forms import Form

class Email(forms.Form):
    subject=forms.CharField(max_length=200,label='subject')
    message=forms.CharField(widget=forms.Textarea,label='message')
    subject.widget.attrs['class']='form-control'
    message.widget.attrs['class']='form-control'
