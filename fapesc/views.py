from django.shortcuts import render, render_to_response
from django.contrib.auth import authenticate, logout, login as authlogin
from django.http.response import HttpResponse
from django.template import Context, loader, RequestContext
from django.contrib.auth.decorators import login_required
from .models import relacao, objeto, restricao, casos
from .forms import UsuarioForm


def inicial(request):
    return render(request, 'pages/index.html')

def cadastro(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)

        if form.is_valid():
            form.formacao = request.POST.get('formacao')
            form.save(commit=True)
            return inicial(request)
        else:
            print(form.errors)
    else:
        form = UsuarioForm()

    return render(request, 'pages/cadastro.html', {'form': form})

def login(request):
    if request.user.id:
        return render_to_response('pages/logado/inicial.html',(),context_instance=RequestContext(request,()))

    if request.POST:
        emailUser = request.POST.get('email')
        senhaUser = request.POST.get('senha')
        u = authenticate(username=emailUser, password=senhaUser)
        if u is not None:
            if u.is_active:
                authlogin(request, u)

                if request.POST.get('next'):
                    return HttpResponseRedirect(request.POST.get('next'))

                return render_to_response('pages/logado/inicial.html',(),context_instance=RequestContext(request, ()))
    return inicial(request)

@login_required
def sair(request):
    logout(request)
    return inicial(request)

@login_required
def caso(request):
    context_dict = {}
    relacaoList = relacao.objects.order_by('-nome')
    objetosList = objeto.objects.order_by('-nome')
    restricaoList = restricao.objects.order_by('-distancia')

    context_dict['relacoes'] = relacaoList
    context_dict['objetos'] = objetosList
    context_dict['restricoes'] = restricaoList

    return render(request, 'pages/caso.html', context_dict)

@login_required
def resultadoCaso(request):
    peso = [0.2, 0.1, 0.2]
    if request.POST:
        objeto1 = request.POST.get('objeto1')
        relacao = request.POST.get('relacao')
        objeto2 = request.POST.get('objeto2')
        distancia = request.POST.get('distancia')
    novoCaso = [objeto1, relacao, objeto2, distancia]
    peso = [0.2, 0.1, 0.2]
    resultado = []
    #restricao = []
    def EhIgual(x, y):
        peso = 0
        if (x == y):
            peso = 0
        else:
            peso = 1
        return peso

    def distancia(peso, caso, novoProblema):
        pesoInstancias = []
        distancia = 0.0
        for i in range(0, len(peso)):
            pesoInstancias.append(EhIgual(caso[i], novoProblema[i]))
        for i in range(0, len(peso)):
            distancia += (peso[i] * pesoInstancias[i])
        distancia = distancia
        resultado = [caso, novoProblema, distancia]
        return resultado

    casolist = casos.objects.order_by('-id')
    restricaoList = restricao.objects.order_by('-id')
    for caso in casolist:
        for restr in restricaoList:
            if (caso.restricao == restr.descricao):
                velhoCaso = [caso.objeto1, caso.relacao, caso.objeto2, restr.distancia, caso.resultado, caso.plano_acao]
                pass
            else:
                velhoCaso =[caso.objeto1, caso.relacao, caso.objeto2, caso.distancia, caso.resultado, caso.plano_acao]
        resultado.append(distancia(peso, velhoCaso, novoCaso))
    return render(request, 'pages/resultadoCaso.html', {"resultado": resultado})