"""salimossss URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include

from iniciosalimos.views import cine_list, detalle_cine_list, festi_list, detalle_festi_list, \
    crio_list, detalle_crio_list, gastro_list, detalle_gastro_list, \
    teatro_list, detalle_teatros_list, toques_list, detalle_toques_list, boli_list, detalle_boli_list, \
    artdep_list, detalle_artdep_list, conamigos_list, enfamilia_list, ninos_list, paseos_list, \
    turismo_list, airlib_list, montevideo_eventos_list, montevideo_inicio_list, montevideo_lugares_list, \
    rocha_eventos_list, rocha_inicio_list, rocha_lugares_list, detalle_eventos_list, detalle_lugares_list, \
    Detalleenfamilia_list, BuscarView, Detalleconamigos_list, Detalleninos_list, Detallepaseos_list, Detalleturismo_list, Comentar_id, Departamento_opciones, Departamento_eventos_list,Departamento_lugares_list, Comentar_todo

from iniciosalimos.views import inicio
from perfiles.views import SignUpView, SignInView, SignOutView, base

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', inicio, name='inicio'),
    path('Cine', cine_list, name='Cinellama'),
    path('Festivales', festi_list, name='Festillama'),
    path('Criollas', crio_list, name='Criollama'),
    path('Gastronomia', gastro_list, name='Gastrollama'),
    path('Teatros', teatro_list, name='Teatrollama'),
    path('Toques', toques_list, name='Toquesllama'),
    path('Boliches',boli_list, name='Bolillama'),
    path('Artdep', artdep_list, name='Artdepllama'),
    path('EnFamilia', enfamilia_list, name='familia'),
    path('Conamigos', conamigos_list, name='amigos'),
    path('ninos', ninos_list, name='ninos'),
    path('paseos', paseos_list, name='paseo'),
    path('Turismo', turismo_list, name='turi'),
    path('airelibre', airlib_list, name='aire'),
    path('Montevideo_inicio', montevideo_inicio_list, name='montevideo_inicio'),
    path('Montevideo_eventos', montevideo_eventos_list, name='montevideo_eventos'),
    path('Montevideo_lugares', montevideo_lugares_list, name='montevideo_lugares'),
    path('Rocha_inicio', rocha_inicio_list, name='rocha_inicio'),
    path('Rocha_eventos', rocha_eventos_list, name='rocha_eventos'),
    path('Rocha_lugares', rocha_lugares_list, name='rocha_lugares'),
    path('Detalle_eventos', detalle_eventos_list, name='detalle_eventos'),
    path('Detalle_lugares', detalle_lugares_list, name='detalle_lugares'),
    path('Detalle_Gastronomia', detalle_gastro_list, name='Detalle_Gastronomia'),
    path('Detalle_Festivales', detalle_festi_list, name='Detalle_Festivales'),
    path('Detalle_Criollas', detalle_crio_list, name='Detalle_Criollas'),
    path('Detalle_Cine', detalle_cine_list, name='Detalle_Cine'),
    path('Detalle_Teatros', detalle_teatros_list, name='Detalle_Teatros'),
    path('Detalle_Toques', detalle_toques_list, name='Detalle_Toques'),
    path('Detalle_Boliches', detalle_boli_list, name='Detalle_Boliches'),
    path('Detalle_Artdep', detalle_artdep_list, name='Detalle_Artdep'),
    path('Detalle_Enfamilia', Detalleenfamilia_list, name='Detalle_enfamilia'),
    url('templates/eventos/', BuscarView.as_view(), name='buscar'),
    path('Detalle_Conamigos', Detalleconamigos_list, name='Detalle_conamigos'),
    path('Detalle_Ninos', Detalleninos_list, name='Detalle_Ninos'),
    path('Detallepaseo', Detallepaseos_list, name='Detallepaseo'),
    path('Detalleturi', Detalleturismo_list, name='Detalleturi'),
    path('Comentar_id', Comentar_id, name='Comentar_id'),
    path('Departamento_opciones', Departamento_opciones, name='Departamento_opciones'),
    path('Departamento_eventos_list', Departamento_eventos_list, name='Departamento_eventos_list'),
    path('Departamento_lugares_list', Departamento_lugares_list, name='Departamento_lugares_list'),
    url(r'^admin/', admin.site.urls),
    #url(r'^$', BienvenidaView.as_view(), name='bienvenidos'),
    url(r'^registrate/$', SignUpView.as_view(), name='sign_up'),
    url(r'^incia-sesion/$', SignInView.as_view(), name='sign_in'),
    url(r'^cerrar-sesion/$', SignOutView.as_view(), name='sign_out'),
    path('base', base, name='base'),
    path('Comentar_todo', Comentar_todo, name='Comentar_todo'),
    path('accounts/', include('allauth.urls')),
    ]
