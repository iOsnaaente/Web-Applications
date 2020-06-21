from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path(''             , views.home        , name='home'),
    path('programacao/' , views.programacao , name='programacao'),
    path('sites/'       , views.web         , name='web'),
    path('supervisorio/', views.supervisorio, name='supervisorio'),
    path('jogos/'       , views.jogos       , name='jogos'),
    path('contato/'     , views.contato     , name='contato'),
    path('sobre/'       , views.sobre       , name='sobre'),
    path('projeto/'     , views.projeto    , name='projetos'),
    
]