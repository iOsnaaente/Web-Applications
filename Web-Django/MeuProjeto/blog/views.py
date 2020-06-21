from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Post, Project

# Create your views here.


def home(request):
    posts = Post.objects.all().order_by('-created_at')
    return render(request, 'blog/home.html', {'posts':posts})

def projeto(request, slug):
    proj = get_object_or_404(Project, slug=slug)
    return render(request, 'blog/projeto.html', {'proj': proj})

def programacao(request):
    proj = Project.objects.all().order_by('-created_at')
    return render(request, 'blog/programacao.html', {'proj':proj})

def web(request):
    return render(request, 'blog/web.html')

def supervisorio(request):
    return render(request, 'blog/supervisorio.html')

def jogos(request):
    return render(request, 'blog/jogos.html')

def contato(request):
    return render(request, 'blog/contato.html')
    
def sobre(request):
    return render(request, 'blog/sobre.html')




