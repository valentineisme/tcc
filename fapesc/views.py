from django.shortcuts import render, render_to_response
from django.contrib.auth import authenticate, logout, login as authlogin
from django.http.response import HttpResponse, HttpResponseRedirect
from django.template import Context, loader, RequestContext
from django.contrib.auth.decorators import login_required
from .models import relacao, objeto, restricao, casos, comunidade, imagem
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
def caso_area(request):
    return render(request, 'pages/logado/caso_comunidade.html')

@login_required
def cadastroComu(request):
    if request.POST:
        nome = request.POST.get('nome_comu')
        bairro = request.POST.get('bairro')
        cidade = request.POST.get('cidade')
        estado = request.POST.get('estado')
        c = comunidade(nome=nome, bairro=bairro, cidade=cidade, estado=estado,teste = nome)
        c.save()
        return render(request, 'pages/logado/caso_imagem.html', {'nome':nome})

@login_required
def cadastroImagem(request):
    if request.POST:
        comunidadeList = comunidade.objects.order_by('-id')
        for comu in comunidadeList:
            if comu.nome == request.POST.get('nome_comu'):
                #imagem = request.POST.get('imagem')
                data = request.POST.get('data')
                lati = request.POST.get('lati')
                longi = request.POST.get('longi')
                i = imagem(comunidade = comu.id, dataImagem = data, latitude = lati, longitude = longi)
                i.save()

        context_dict = {}
        relacaoList = relacao.objects.order_by('-nome')
        objetosList = objeto.objects.order_by('-nome')
        restricaoList = restricao.objects.order_by('-distancia')

        context_dict['relacoes'] = relacaoList
        context_dict['objetos'] = objetosList
        context_dict['restricoes'] = restricaoList

        return render(request, 'pages/logado/caso.html', {'id':imagem.id}, context_dict)

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
    return render(request, 'pages/logado/resultadoCaso.html', {"resultado": resultado})