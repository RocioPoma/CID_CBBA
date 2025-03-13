from django.forms import ModelForm
from django import forms
from .models import Book,Tesis,Magazine, Favorite, Article
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class BookForm(ModelForm):
    class Meta:
     model = Book
     fields = '__all__'

class TesisForm(ModelForm):
    class Meta:
     model = Tesis
     fields = '__all__'


class CustomUserCreationForm(UserCreationForm):
	email = forms.EmailField(required=True)

	class Meta:
		model = User
		fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']
	def clean_email(self):
		email = self.cleaned_data['email']

		if User.objects.filter(email=email).exists():
			raise forms.ValidationError('Este correo electrónico ya está registrado')
		return email


class MagazineForm(ModelForm):
    class Meta:
     model = Magazine
     fields = '__all__'


class FavoriteForm(ModelForm):
    class Meta:
     model = Favorite
     fields = '__all__'

class ArticleForm(ModelForm):
    class Meta:
     model = Article
     fields = '__all__'