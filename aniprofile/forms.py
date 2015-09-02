from django import forms


class RegistrationForm(forms.Form):
    username = forms.CharField(max_length=30, label="Username", widget=forms.TextInput(
        attrs={'required': 'required'}))
    password = forms.CharField(max_length=200, widget=forms.PasswordInput(
        attrs={'required': 'required'}), label="Password")
    passwordConfirm = forms.CharField(max_length=200, widget=forms.PasswordInput(
        attrs={'required': 'required'}), label="Confirm Password")
    email = forms.EmailField(label="Email Address", widget=forms.TextInput(
        attrs={'required': 'required', 'placeholder': 'Enter a Email Valid Address'}))
    test = forms.CharField(max_length=6, label="What University is this Club based out of?",
        widget=forms.TextInput(attrs={'required': 'required'}))