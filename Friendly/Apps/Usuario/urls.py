from django.urls import path
from .views import Formulario,Inicio,RecetaReposteria,RecetaTradicional,RecetaVegana


urlpatterns = [
    path('', Inicio, name='Inicio' ),
    path('Usuario/Formulario.html/', Formulario, name='Formulario' ),
    path('Usuario/RecetaTradicional.html/', RecetaTradicional, name='RecetaTradicional'),
    path('Usuario/RecetaVegana.html/', RecetaVegana, name='RecetaVegana'),
    path('Usuario/RecetaReposteria.html/', RecetaReposteria, name='RecetaResposteria'),

]
