from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('RegistroUsuarios/', views.index, name='index'),
    path ('ciudades/', views.ciudades, name='ciudades'),  
    path('ciudades/new/', views.new_ciudad, name='new_ciudades'),
    path('tipodocumentos/',views.tipodocumentos,name='tipodocumentos'),
    path('tipodocumentos/new',views.new_tipodocumento,name='new_tipodocumentos'),
    path('personas/',views.personas,name='personas'),
    path('personas/new',views.new_persona,name='new_persona'),
]