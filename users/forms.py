from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
import uuid

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'name', 'full_name', 'phone', 'password')

        widgets = {
            'username': forms.TextInput(),
            'email': forms.EmailInput(),
            'name': forms.TextInput(),
            'full_name': forms.TextInput(),
            'phone': forms.NumberInput(),
            'password': forms.PasswordInput()
        }

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'name', 'full_name', 'phone', 'password')

        widgets = {
            'username': forms.TextInput(),
            'email': forms.EmailInput(),
            'name': forms.TextInput(),
            'full_name': forms.TextInput(),
            'phone': forms.NumberInput(),
            'password': forms.PasswordInput()
        }

class RegisterForm(forms.ModelForm):
    class Meta:
        model = get_user_model()
        fields = ('username', 'email', 'name', 'full_name', 'phone', 'password')

        widgets = {
            'username': forms.TextInput(),
            'email': forms.EmailInput(),
            'name': forms.TextInput(),
            'full_name': forms.TextInput(),
            'phone': forms.NumberInput(),
            'password': forms.PasswordInput()
        }
    
    def saveUserClient(self):
        username = self.cleaned_data.get('username')
        email = self.cleaned_data.get('email')
        name = self.cleaned_data.get('name')
        full_name = self.cleaned_data.get('full_name')
        password = self.cleaned_data.get('password')
        phone = self.cleaned_data.get('phone')
        User = get_user_model()
        user = User.objects.create_user(
            username=username,
            email=email,
            name=name,
            full_name=full_name,
            password=password,
            phone=phone
        )
        user.is_active = False
        user.verification_code = uuid.uuid1().hex[:8]
        return user.save()