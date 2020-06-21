from bricks.models import * 
from peewee import *


def repetido(nome, classe, classificacao):
	# PROCURAR O NOME NO BANCO DE DADOS
	try:
		classe.get(classificacao == nome ).get()
	except:
		return True
	return False


def arroba(email):
	#PROCURA UM @ NO EMAIL PARA VALIDAR
	aux = email.split("@")
	if (aux[0]!=email and len(aux)==2):
	    return True
	else:
	    return False


def busca(nome, classe, classificacao):
	aux =  classe.get(classificacao == nome).get()
	return aux

