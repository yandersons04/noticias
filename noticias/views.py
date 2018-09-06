from django.shortcuts import render
from .models import Artigo
from django.utils import timezone


def art_list(request):
    artigos = Artigo.objects.filter(data_publicado__lte=timezone.now()).order_by('data_publicado')
    return render(request, 'noticias/art_list.html', {'artigos': artigos})