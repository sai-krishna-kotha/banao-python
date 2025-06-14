from django import forms
from .models import CustomUser
from django.contrib.auth.hashers import make_password

class SignupForm(forms.ModelForm):
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control form-control-sm py-1'
        })
    )
    confirm_password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control form-control-sm py-1',
        })
    )

    class Meta:
        model = CustomUser
        fields = [
            'first_name', 'last_name', 'profile_picture', 'username', 'email',
            'user_type', 'address_line1', 'city', 'state', 'pincode',
        ]
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control form-control-sm py-1','required':True}),
            'last_name': forms.TextInput(attrs={'class': 'form-control form-control-sm py-1','required':True}),
            'profile_picture': forms.ClearableFileInput(attrs={'class': 'form-control form-control-sm py-1','required':True}),
            'username': forms.TextInput(attrs={'class': 'form-control form-control-sm py-1','required':True}),
            'email': forms.EmailInput(attrs={'class': 'form-control form-control-sm py-1','required':True}),
            'address_line1': forms.TextInput(attrs={'class': 'form-control form-control-sm py-1','required':True}),
            'city': forms.TextInput(attrs={'class': 'form-control form-control-sm py-1','required':True}),
            'state': forms.TextInput(attrs={'class': 'form-control form-control-sm py-1','required':True}),
            'pincode': forms.TextInput(attrs={'class': 'form-control form-control-sm py-1','required':True}),
            'user_type': forms.Select(attrs={'class': 'form-select form-select-sm py-1','required':True}),
        }

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password and confirm_password and password != confirm_password:
            self.add_error('confirm_password', "Passwords do not match")

        return cleaned_data

    def save(self, commit=True):
        user = super().save(commit=False)
        user.password = make_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user


class LoginForm(forms.Form):
    username = forms.CharField(
        label='Username',
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'form-control form-control-sm py-1',
        })
    )
    
    password = forms.CharField(
        required=True,
        widget=forms.PasswordInput(attrs={
            'class': 'form-control form-control-sm py-1',
        })
    )
    
    user_type = forms.ChoiceField(
        choices=(('','---------'),('doctor', 'Doctor'), ('patient', 'Patient')),
        label='Login as',
        widget=forms.Select(attrs={
            'class': 'form-select form-select-sm py-1'
        })
    )
