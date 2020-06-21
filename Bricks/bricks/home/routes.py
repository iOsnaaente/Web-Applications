from werkzeug.security import generate_password_hash, check_password_hash
from bricks.models import Usuario, Itens, Imagens, db, Lances
from flask import request, render_template, session
from flask import Flask, url_for
from bricks.home import home_bp



@home_bp.route('/home', methods = ['GET', 'POST'])
def home():
    if session['nome'] != 0:
        return render_template("home.html")
    else:
        return render_template("cadastrar-se.html")


@home_bp.route('/lances', methods = ['GET', 'POST'])
def lances():
    return render_template("lance.html")


@home_bp.route("/meus_itens", methods = ["GET", "POST"])
def meus_itens():
    if session["nome"] == 0:
        return render_template("cadastrar-se.html")
    else:
        queryU = Usuario.get(Usuario.usuario_login == session['nome'])

        selecionarItens = Itens.select().where(Itens.itens_id_users_id == queryU.id)
        
        s=[]
        for a in selecionarItens:
            

            selecionarImagens = Imagens.select().where(Imagens.imagens_id_itens_id == a.id)
            imagem=[]
            t=0
            for teste in selecionarImagens:
                imagem.insert(t, teste.imagens_name_hash)
                t+=1
            b = {
                    
                    'id': a.id,
                    'id_user_lancador': a.itens_id_users_id, 
                    'id_user_alvo': request.args.get('id_user_alvo'),
                    'id_item_alvo': request.args.get('id_item_alvo'),
                    'titulo': a.itens_titulo,
                    'descricao': a.itens_descricao,
                    'imagens': imagem
                    
                    }    
            s.append(b)
        print(s)

        return render_template('carregar_oferta.html',si = s)



@home_bp.route('/incluir_item', methods = ['GET', 'POST'])
def incluir_item():
    if session["nome"] == 0:
        return render_template("cadastrar-se.html")
    else:
        return render_template('incluir_item.html')


@home_bp.route('/logout', methods = ['GET', 'POST'])
def logout():
    if session["nome"] ==0:
        return render_template("cadastrar-se.html")
    else:
        session["nome"] = 0
        return render_template('logout.html')



@home_bp.route('/pesquisa', methods = ['GET', 'POST'])
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


@home_bp.route('/carregar_oferta/', methods = ['GET', 'POST'])
def carregar_oferta():
    try:
        queryU = Usuario.get(Usuario.usuario_login == session['nome'])

        selecionarItens = Itens.select().where(Itens.itens_id_users_id == queryU.id)
        
        s=[]
        for a in selecionarItens:
            

            selecionarImagens = Imagens.select().where(Imagens.imagens_id_itens_id == a.id)
            imagem=[]
            t=0
            for teste in selecionarImagens:
                imagem.insert(t, teste.imagens_name_hash)
                t+=1
            b = {
                    
                    'id': a.id,
                    'id_user_lancador': a.itens_id_users_id, 
                    'id_user_alvo': request.args.get('id_user_alvo'),
                    'id_item_alvo': request.args.get('id_item_alvo'),
                    'titulo': a.itens_titulo,
                    'descricao': a.itens_descricao,
                    'imagens': imagem
                    
                    }    
            s.append(b)
        print(s)

        return render_template('carregar_oferta.html',si = s)
    except:
        return render_template("cadastrar-se.html")