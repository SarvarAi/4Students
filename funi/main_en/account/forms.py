from django import forms


class Signup1Form(forms.Form):
    first_name = forms.CharField(max_length=255, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'id': 'floatingInput',
        'placeholder': 'Your name'
    }))

    last_name = forms.CharField(max_length=255, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'id': 'floatingInput',
        'placeholder': 'Your surname'
    }))

    middle_name = forms.CharField(max_length=255, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'id': 'floatingInput',
        'placeholder': 'Middle name'
    }))


class Signup2Form(forms.Form):
    username = forms.CharField(max_length=255, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'id': 'floatingInput',
        'placeholder': 'Create username'
    }))

    telephone_number = forms.CharField(max_length=255, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'id': 'floatingInput',
        'placeholder': 'Your phone number'
    }))

    date_of_birth = forms.DateField(widget=forms.DateInput(attrs={
        'class': 'form-control',
        'id': 'floatingInput',
        'placeholder': 'Birth',
        'type': 'date'
    }))

    email = forms.EmailField(max_length=255, widget=forms.EmailInput(attrs={
        'class': 'form-control',
        'id': 'floatingInput',
        'placeholder': 'Enter your email address'
    }))


class Signup3Form(forms.Form):
    password1 = forms.CharField(max_length=255, widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'id': 'floatingPassword',
        'placeholder': 'Create password'
    }))

    password2 = forms.CharField(max_length=255, widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'id': 'floatingPassword',
        'placeholder': 'Confirm your password'
    }))


class AccountSettingsForm(forms.Form):
    first_name = forms.CharField(max_length=255, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'type': 'text'
    }))

    last_name = forms.CharField(max_length=255, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'type': 'text'
    }))

    middle_name = forms.CharField(max_length=255, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'type': 'text'
    }))

    email = forms.EmailField(max_length=255, widget=forms.EmailInput(attrs={
        'class': 'form-control',
    }))

    extra_email = forms.EmailField(max_length=255, required=False, widget=forms.EmailInput(attrs={
        'class': 'form-control',
    }))

    telephone_number = forms.CharField(max_length=255, widget=forms.TextInput(attrs={
        'class': 'form-control'
    }))

    extra_telephone_number = forms.CharField(max_length=255, required=False, widget=forms.TextInput(attrs={
        'class': 'form-control'
    }))

    bio = forms.CharField(max_length=255, widget=forms.Textarea(attrs={
        'class': 'form-control',
        'rows': '4'
    }))


class PasswordSettingsForm(forms.Form):
    old_password = forms.CharField(max_length=255, widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'type': 'password'
    }))

    new_password = forms.CharField(max_length=255, widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'type': 'password'
    }))

    confirm_password = forms.CharField(max_length=255, widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'type': 'password'
    }))


class DetailedCheckForm(forms.Form):
    ...
