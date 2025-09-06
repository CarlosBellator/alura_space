from django.shortcuts import render

def index(request):
    dados = {
            1: {
                'nome': 'Nebulósa de Carina',
                'legenda': 'webtelescope.org / NASA / James Webb',
            },
            2: {
                'nome': 'Exploração de Marte',
                'legenda': 'webtelescope.org / NASA / Perseverance',
            }
    }
    return render(request, 'galeria/index.html', {'cards': dados})

def imagem(request):
    return render(request, 'galeria/imagem.html')