from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(
        max_length=254,
        help_text='Введите действительный email'
    )

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if len(username) < 8:
            raise forms.ValidationError('Имя пользователя должно содержать не менее 8 символов.')
        return username

    def clean_password1(self):
        password1 = self.cleaned_data.get('password1')
        if len(password1) < 8:
            raise forms.ValidationError('Пароль должен содержать не менее 8 символов.')
        return password1

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if email:
            email = email.lower()
        return email


class LoginForm( forms.Form ):
    username = forms.CharField( max_length=100,label="Имя пользователя",widget=forms.TextInput({'placeholder' : 'Имя пользователя'}))
    password = forms.CharField( max_length=100, label='Пароль', widget=forms.PasswordInput({'placeholder' : 'Пароль'}))

