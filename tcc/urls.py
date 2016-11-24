from django.conf.urls import include, url
from django.contrib import admin
from fapesc import views

urlpatterns = [
    # Examples:
    # url(r'^$', 'tcc_final.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^inicial/', views.inicial, name='inicial'),
    url(r'^cadastro/$', views.cadastro, name='cadastro'),
    url(r'^validacao/$', views.login, name='login'),
    url(r'^sair/$', views.sair, name='sair'),
    url(r'^area/$', views.caso_area, name='area'),
    url(r'^comunidade/$', views.cadastroComu, name='comunidade'),
    url(r'^imagem/$', views.cadastroImagem, name='imagem'),
    #url(r'^caso/', views.caso, name='caso'),
    url(r'^resultado/', views.resultadoCaso, name='resultadoCaso'),
]
