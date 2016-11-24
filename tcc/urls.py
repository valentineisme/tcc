from django.conf.urls import include, url
from django.contrib import admin
from fapesc import views

urlpatterns = [
    # Examples:
    # url(r'^$', 'tcc_final.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^login/$', views.login, name='login'),
    url(r'^index/', views.index, name='index'),
    url(r'^inicial/', views.inicial, name='inicial'),
    url(r'^CadUser/$', views.CadUser, name='CadUser'),
    url(r'^validacao/$', views.validacao, name='validacao'),
    url(r'^sair/$', views.sair, name='sair'),
    url(r'^area/$', views.caso_area, name='area'),
    url(r'^CadComunidade/$', views.CadComunidade, name='CadComunidade'),
    url(r'^CadImagem/$', views.CadImagem, name='CadImagem'),
    #url(r'^caso/', views.caso, name='caso'),
    url(r'^resultado/', views.resultadoCaso, name='resultadoCaso'),
]
