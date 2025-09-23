from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User, Group

class SignUpForm(UserCreationForm):
    email = forms.EmailField(required=True,widget=forms.EmailInput(attrs={"class": "form-control"}))
    ROLE_CHOICES = (("student","Student"),("admin","Admin"))
    role = forms.ChoiceField(choices=ROLE_CHOICES)

    class Meta:
        model = User
        fields = ("username", "email", "role", "password1", "password2")
        widgets = {
            "username": forms.TextInput(attrs={"class": "form-control"}),
            "password1": forms.PasswordInput(attrs={"class": "form-control"}),
            "password2": forms.PasswordInput(attrs={"class": "form-control"}),
        }
    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
            role = self.cleaned_data["role"]
            group, created = Group.objects.get_or_create(name=role)
            user.groups.add(group)
        return user