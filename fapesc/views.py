from django.shortcuts import render, render_to_response
from django.contrib.auth import authenticate, logout, login as authlogin
from django.http.response import HttpResponse, HttpResponseRedirect
from django.template import Context, loader, RequestContext
from django.contrib.auth.decorators import login_required
from .models import relacao, objeto, restricao, casos, comunidade, imagem, usuario
from .forms import UsuarioForm, ComunidadeForm, ImagemForm, CasoForm


def index(request):
    return render(request, 'index.html')
def inicial(request):
    return render(request, 'inicial.html')
def login(request):
    return render(request, 'login.html')

def CadUser(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)

        if form.is_valid():
            form.formacao = request.POST.get('formacao')
            form.save(commit=True)
            return index(request)
        else:
            print(form.errors)
    else:
        form = UsuarioForm()

    return render(request, 'CadUser.html', {'form': form})

def validacao(request):
    if request.user.id:
        return render_to_response('index.html',(),context_instance=RequestContext(request,()))

    if request.POST:
        emailUser = request.POST.get('email')
        senhaUser = request.POST.get('senha')

        u = authenticate(username=emailUser, password=senhaUser)
        if u is not None:
            if u.is_active:
                authlogin(request, u)

                if request.POST.get('next'):
                    return HttpResponseRedirect(request.POST.get('next'))

                return render_to_response('index.html',(),context_instance=RequestContext(request, ()))
    return login(request)



@login_required
def FormComunidade(request):
    form = ComunidadeForm()
    return render(request, 'FormComunidade.html', {'form': form})

@login_required
def CadComunidade(request):

    if request.POST:
        form = ComunidadeForm(request.POST)

        if form.is_valid():
            post = form.save(commit=False)

            post.save()
            id_comunidade = post.id
            print (id_comunidade)

            return HttpResponseRedirect('/FormImagem/'+str(id_comunidade))
            # print (id_comunidade)
            # return render_to_response('FormImagem.html',{'id_comunidade': id_comunidade},context_instance=RequestContext(request))
            # return render(request, self.template, {'form': form, 'method': 'get', 'id': id})
            # return render(request, 'FormImagem.html', {'form':form, 'method':'get', 'id_segurado': id_comunidade})
        else:
            print(form.errors)
        return render(request, 'FormComunidade.html', {'form': form, 'method': 'post'})
@login_required
def FormImagem(request, id_comunidade=None):
    # print ('bla' + request.POST.get('id_comunidade'))
    if id_comunidade:
        nome_comunidade = comunidade.objects.get(id=id_comunidade)
        id_comunidade = id_comunidade
        print (id_comunidade)
    else:
        id_comunidade = None
    form = ImagemForm()
    form.comunidade = id_comunidade
    return render(request, 'FormImagem.html', {'form': form, 'id_comunidade': id_comunidade})

@login_required
def CadImagem(request):
    if request.POST:
        form = ImagemForm(request.POST, request.FILES)
        print (request.FILES)
        if form.is_valid():
            post = form.save(commit=False)

            post.save()
            id_imagem = post.id
            return HttpResponseRedirect('/BuscarCaso/'+str(id_imagem))
        else:
            print(form.errors)
        return render(request, 'FormImagem.html', {'form': form, 'method': 'post'})
@login_required
def FormCaso(request):
    form = CasoForm()
    return render(request, 'FormCaso.html', {'form': form})
def CadCaso(request):
    if request.POST:
        form = CasoForm(request.POST)
        #print(form.id_usuario_id)
        if form.is_valid():
            post = form.save(commit=False)
            current_user = usuario.objects.get(nome=request.user)
            print(current_user.id)
            post.id_usuario = current_user

            post.save()
            return render(request, 'index.html')
        else:
            print(form.errors)
        return render(request, 'FormCaso.html', {'form': form, 'method': 'post'})


@login_required
def resultadoCaso(request):
    peso = [0.2, 0.1, 0.2]
    if request.POST:
        objeto1 = request.POST.get('objeto1')
        relacao = request.POST.get('relacao')
        objeto2 = request.POST.get('objeto2')
        distancia = request.POST.get('distancia')
    novoCaso = [str(objeto1), str(relacao), str(objeto2), str(distancia)]
    peso = [0.8, 0.4, 0.8]
    resultado = []
    def EhIgual(x, y):
        if (x == y):
            peso = 0
        else:
            peso = 1
        return peso

    def distancia(peso, caso, novoProblema):
        pesoInstancias = []
        distancia = 0.0
        for i in range(0, len(peso)):
            pesoInstancias.append(EhIgual(str(caso[i]), novoProblema[i]))
        for i in range(0, len(peso)):
            distancia += (peso[i] * pesoInstancias[i])
        distancia = distancia
        resultado = [caso, novoProblema, distancia]
        return resultado

    casolist = casos.objects.order_by('-id')
    for caso in casolist:
        velhoCaso = [str(caso.objeto1), str(caso.relacao), str(caso.objeto2), caso.distancia, str(caso.resultado), str(caso.plano_acao)]
        resultado.append(distancia(peso, velhoCaso, novoCaso))
    return render(request, 'resultadoCaso.html', {"resultado": resultado})

@login_required
def sair(request):
    logout(request)
    return index(request)