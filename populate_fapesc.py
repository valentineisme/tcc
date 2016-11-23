import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tcc.settings')

import django
django.setup()

from fapesc.models import relacao, restricao, objeto


def populate():
    add_objeto(nome="Floresta",)
    add_objeto(nome="Reflorestamento",)
    add_objeto(nome="Campo",)
    add_objeto(nome="Terras Aridas",)
    add_objeto(nome="Recursos Hidricos (Doce)",)
    add_objeto(nome="Recursos Hidricos (Salobra)",)
    add_objeto(nome="Cultivo",)
    add_objeto(nome="Mineracao",)
    add_objeto(nome="Construcao",)
    add_objeto(nome="Ferrovia",)
    add_objeto(nome="Rodovia",)

    add_relacao(nome="Perto de",)
    add_relacao(nome="Toca",)
    add_relacao(nome="Sobrepoe",)
    add_relacao(nome="Igual",)
    add_relacao(nome="Dentro de",)
    add_relacao(nome="Contem",)

    add_restricao(descricao="Res01: Art20. Faixas Rodoviarias: 200m, ambos os lados", distancia=200,)
    add_restricao(descricao="Res03: Art9. Construcoes que causam riscos devem ficar 200m dos recursos hidricos", distancia=200,)
    add_restricao(descricao="Res04: Art44. 500m de largura em torno de parques estaduais, estacoes ecologicas e reservas biologicas", distancia=500,)
    add_restricao(descricao="Res05: de 10 (dez) metros, para rios de largura inferior a 20 (vinte) metros", distancia=10,)
    add_restricao(descricao="Res07: Lagoas e Lagos: 100m", distancia=100,)
    add_restricao(descricao="Res08: Nascentes: 50m", distancia=50,)

def add_objeto(nome):
    o = objeto.objects.get_or_create(nome=nome)[0]
    o.save()
    return o

def add_relacao(nome):
    r= relacao.objects.get_or_create(nome=nome)[0]
    r.save()
    return r

def add_restricao(descricao, distancia=0):
    res = restricao.objects.get_or_create(descricao = descricao, distancia = distancia)[0]
    res.save()
    return res

# Start execution here!
if __name__ == '__main__':
    print ("Starting Rango population script...")
    populate()
