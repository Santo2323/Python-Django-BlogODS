from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .models import Ods, Posts, Comentarios
from .forms import Formulario_alta_post, NuevoComentario
# si la vista es basada en funcion
from django.contrib.auth.decorators import login_required

#si la vista es basada en clase
from django.contrib.auth.mixins import LoginRequiredMixin


class AltaPost(LoginRequiredMixin,CreateView):
	model= 'Posts'
	template_name = 'Posts/alta.html'
	form_class = Formulario_alta_post
	success_url= reverse_lazy('primera_vista')


def filtro(request, pk):
	p = Posts.objects.filter(Ods = pk)
	
	ctx = {}
	ctx['posts'] = p
	o = Ods.objects.all()
	ctx['Ods'] = o
	
	return render (request,'Posts/Filtro.html',ctx)	


def DetallePost(request, pk):

	p = Posts.objects.get(pk = pk)
	ctx = {}
	ctx['posts'] = p
	o = Ods.objects.all()
	ctx['Ods'] = o
	comments = p.comments.filter(status=True)
	SoloEstePost = None

	if request.method == 'POST':
		comment_form = NuevoComentario(request.POST,)
		if comment_form.is_valid():
			SoloEstePost = comment_form.save(commit=False)
			SoloEstePost.Posts = p
			SoloEstePost.save()
			
	else:
		comment_form = NuevoComentario()
	return render(request, 'Posts/detallePost.html', {'p': p, 'comments': SoloEstePost, 'comments': comments, 'comment_form': comment_form, 'posts': p, 'Ods': o})
