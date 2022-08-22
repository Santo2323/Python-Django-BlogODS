from django.shortcuts import render, redirect 
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm
from apps.posts.models import Ods, Posts

def Inicio(request):
	p = Posts.objects.all()
	ctx = {}
	ctx['posts'] = p

	o = Ods.objects.all()
	ctx['Ods'] = o
	
	return render (request,'Base.html',ctx)



def register(request):
	if request.method == 'POST':
		form = UserRegisterForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data['username']
			messages.success(request, f'Usuario {username} creado')
			return redirect('login')
	else:
		form = UserRegisterForm()
	context = { 'form' : form }
	return render(request, 'usuarios/register.html', context)


