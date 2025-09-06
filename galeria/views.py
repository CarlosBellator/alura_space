from django.shortcuts import render, get_object_or_404
from galeria.models import Fotografia

def index(request):
    # Exemplo de dados:
    # dados = {
    #     1: {
    #         'nome': 'Nebulósa de Carina',
    #         'legenda': 'webtelescope.org / NASA / James Webb',
    #     },
    #     2: {
    #         'nome': 'Exploração de Marte',
    #         'legenda': 'webtelescope.org / NASA / Perseverance',
    #     }
    # }
    fotografias = Fotografia.objects.all()
    return render(request, 'galeria/index.html', {'cards': fotografias})

def imagem(request, foto_id):
    fotografia = get_object_or_404(Fotografia, pk=foto_id)
    return render(request, 'galeria/imagem.html', {"fotografia": fotografia})