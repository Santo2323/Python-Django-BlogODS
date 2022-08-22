from django.urls import path
from . import views 

app_name='posts'

urlpatterns = [
    path('Alta/', views.AltaPost.as_view(),name='alta_post'),
    path('filtro/<int:pk>', views.filtro, name = 'filtro'),
    path('detalle/<int:pk>', views.DetallePost, name= 'detalle'),
]
