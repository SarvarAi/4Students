from django import forms
from .models import FAQ


class FAQForm(forms.ModelForm):
    first_name = forms.CharField(max_length=255, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'id': 'firstName',
        'type': 'text'
    }))

    last_name = forms.CharField(max_length=255, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'id': 'lastName',
        'type': 'text'
    }))

    email = forms.EmailField(max_length=255, widget=forms.EmailInput(attrs={
        'class': 'form-control',
        'type': 'text',
        'id': 'email',
        'placeholder': 'Enter your email'
    }))

    second_email = forms.EmailField(max_length=255, required=False, widget=forms.EmailInput(attrs={
        'class': 'form-control',
        'type': 'text',
        'id': 'email',
        'placeholder': 'It is not mandatory'
    }))

    subject = forms.CharField(max_length=255, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'id': 'address',
        'placeholder': 'Enter the subject of your mail',
        'type': 'text'
    }))

    question = forms.CharField(max_length=512, widget=forms.Textarea(attrs={
        'class': 'form-control',
        'id': 'address2',
        'rows': '3'
    }))

    class Meta:
        model = FAQ
        fields = ('first_name',
                  'last_name',
                  'email',
                  'second_email',
                  'subject',
                  'question')


class AuthenticationForm(forms.Form):
    username = forms.CharField(max_length=255, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'id': 'floatingInput',
        'placeholder': 'Enter your username'
    }))

    password = forms.CharField(max_length=255, widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'id': 'floatingPassword',
        'placeholder': 'Password'
    }))
