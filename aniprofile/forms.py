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

    def clean_test(self):
        data = self.cleaned_data['test']
        if data.upper() != "MCGILL":
            raise forms.ValidationError("Incorrect Answer")

    def clean(self):
        cleaned_data = super(RegistrationForm, self).clean()
        password = cleaned_data.get("password")
        password2 = cleaned_data.get("passwordConfirm")
        if password != password2:
            self.add_error('passwordConfirm', forms.ValidationError("Passwords do not match"))