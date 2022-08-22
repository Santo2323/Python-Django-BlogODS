from django import forms
from django.db.models.fields import CommaSeparatedIntegerField
from django.forms import widgets
from .models import Posts, Comentarios
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from apps.usuarios.models import Usuario


class Formulario_alta_post(forms.ModelForm):
	

	class Meta:
		model = Posts
		fields= '__all__'
		widgets = { 
			"nombre": forms.TextInput(attrs={"class": "form-control" }),
			"Body": forms.Textarea(attrs={"class": "form-control"}),
		}


class NuevoComentario(forms.ModelForm):
	
	class Meta:
		model = Comentarios
		fields= ( "name", "body")
		widgets = {
			"name": forms.TextInput(attrs={"class": "col-sm-12"}),
		    "body": forms.Textarea(attrs={"class": "col-sm-12"}),

		}







		

