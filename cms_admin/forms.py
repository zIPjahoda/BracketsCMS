from django import forms

from cms.models import Article, Category, MenuItem, StaticPage
from django.contrib.auth.models import User


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ('title', 'description', 'keywords', 'category', 'content')


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ('title', 'description', 'keywords', 'thumbnail_path')


class MenuItemForm(forms.ModelForm):
    class Meta:
        model = MenuItem
        fields = ('title', 'link')


class StaticPageForm(forms.ModelForm):
    class Meta:
        model = StaticPage
        fields = ('title', 'contents')


class UserLoginForm(forms.Form):
    username = forms.CharField(max_length=30)
    password = forms.CharField(max_length=30, widget=forms.PasswordInput())


class UserRegisterForm(forms.Form):
    username = forms.CharField(label="Username", max_length=30)
    password = forms.CharField(label="Password", widget=forms.PasswordInput())
    password_again = forms.CharField(label="Password check", widget=forms.PasswordInput())
    email = forms.EmailField(label="Email")
    first_name = forms.CharField(label="First name", max_length=40)
    last_name = forms.CharField(label="Last name", max_length=40)

    def create_user_object(self):
        user = User.objects.create_user(self.cleaned_data["username"], self.cleaned_data["email"], self.cleaned_data["password"])
        user.first_name = self.cleaned_data["first_name"]
        user.last_name = self.cleaned_data["last_name"]
        return user
