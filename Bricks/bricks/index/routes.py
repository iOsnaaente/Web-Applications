from werkzeug.security import generate_password_hash, check_password_hash
from bricks.models import Usuario, Itens, Imagens, db, Lances
from flask import request, render_template, session
from bricks.index import index_bp
from flask import Flask, url_for
from bricks.funcoes import *


@index_bp.route('/index', methods = ['GET', 'POST'])
def index():
    try:
        if session["nome"] == 0:
            return render_template("index.html")
        else:
            return render_template("home.html")
    except:
        return render_template("index.html")

@index_bp.route('/login_check', methods = ['GET', 'POST'])
def login_check():

    if request.method == 'POST':
        
        try: 
            query = Usuario.select(Usuario.usuario_login).where(Usuario.usuario_login == request.form.get('nome')).get()

            if('{0.usuario_login}'.format(query) == request.form.get('nome')):

                queryS = Usuario.select(Usuario.usuario_senha)
                print(queryS)

                for aux in queryS:
                    print(aux.usuario_senha)

                    if(check_password_hash (aux.usuario_senha,  request.form.get('senha')) == True):
                        session['nome'] = request.form.get('nome')
                        usuario_local = request.form.get('nome')

                        return render_template('home.html') 
                    else:
                        return render_template("index.html")
        except:
            return render_template('index.html')



@index_bp.route('/cadastro_enviado', methods = ['GET','POST'])
def cadastro_enviado():


    info = {
        "usuario_login"     : request.form.get("usuario"),
        "usuario_nome"      : request.form.get("nome"),
        "usuario_senha"     :generate_password_hash(request.form.get('senha')),
        "usuario_email"     : request.form.get("email"),
        "usuario_cidade"    : request.form.get("cidade"),
        "usuario_estado"    : request.form.get("estado")
        }


    #bool rep = login, email
    rep_login = repetido(info["usuario_login"], Usuario, Usuario.usuario_login)
    rep_email = repetido(info["usuario_email"], Usuario, Usuario.usuario_email)

    #bool arroba = email
    arroba_email = arroba(info["usuario_email"])


    """
    FAZER OS TESTES 
    """
    lista = [rep_email,rep_login,arroba_email]

    if (False in lista):
        return render_template("index.html")

    else:
        Usuario.insert_many(info).execute()
        return render_template("cadastro_enviado.html")



@index_bp.route('/pesquisa', methods = ['GET', 'POST'])
def pesquisa():
   
    if request.method == 'POST':

        procuraTitulo = Itens.select().where(Itens.itens_categoria == request.form.get('pesquisa'))
        d=[]
        for iten in procuraTitulo:
            imagens = Imagens.select().where(Imagens.imagens_id_itens_id == iten.id)
            img=[]            
            j=0
            for imagen in imagens:
               img.insert(j,imagen.imagens_name_hash)
               j+= 1
            e = {
                  
                  'id': iten.id,
                  'id_user': iten.itens_id_users_id,
                  'titulo': iten.itens_titulo,
                  'descricao': iten.itens_descricao,
                  'imagens': img
                } 
            d.append(e)
                   
        quantiO = len(d)

        return render_template('pesquisa.html', resultadoTitulo=d, quantidadeObjetos = quantiO)

    return render_template('index.html')