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
    #url(r'^area/$', views.caso_area, name='area'),
    url(r'^FormComunidade/$', views.FormComunidade, name='FormComunidade'),
    url(r'^CadComunidade/$', views.CadComunidade, name='CadComunidade'),
    url(r'^FormImagem/$', views.FormImagem, name='FormImagem'),
    url(r'^CadImagem/$', views.CadImagem, name='CadImagem'),
    url(r'^FormCaso/', views.FormCaso, name='FormCaso'),
    url(r'^CadCaso/', views.CadCaso, name='CadCaso'),
    url(r'^resultadoCaso/', views.resultadoCaso, name='resultadoCaso'),
]
