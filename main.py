from flask import Flask, render_template, request, redirect, session
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.secret_key = 'fabricio'
app.config['SQLACHEMY_DATABASE_URI'] = "mysql+mysqlconnector://root:''@localhost/filmesteca"
#criação da classe "filme", modo primitivo de armazenar dados da lista
class filme:
    def __init__(self,nome, genero, diretor,ano):
        self.nome = nome
        self.genero = genero
        self.diretor = diretor
        self.ano = ano
#exemplos iniciais pra enriquecer visualmente a experiência de quem entra no site
avatar = filme('avatar 2: caminho', 'aventura/fantasia','james cameron',2022)
joker = filme('joker','drama','todd philips',2019)
jack = filme('o estranho mundo de jack','animação','tim burton',1993)
ldj = filme('liga da justiça','ação','jack snider',2021)
estomago = filme('estomago','drama','marcos jorge',2007)
lista = [avatar,joker,jack,ldj,estomago]

@app.route('/inicio')
def inicio():
    return render_template('index.html',lista=lista)

#só pra página inicial n ficar vazia, poderia ter começado com a lista porém acho feio (não me pergunte pq)
@app.route('/')
def sla():
    return render_template('sla.html')

def vel(session):
    if session == 'verdadeiro':
        return True




#criei pela necessidade e boa prática de encapsular código
#verifica se já tem filme na lista, falso = não tem true = já tem
def verificarro(lista,novo_filme):
    for c in range(len(lista)):
        if lista[c].nome == novo_filme.nome:
            return True
    else:
        return False

@app.route('/catalogar',methods=['POST',])
def catalogar():
    nome = request.form.get('nome_cadastro')
    genero = request.form.get('genero_cadastro')
    diretor = request.form.get('diretor_cadastro')
    ano = request.form.get('ano_cadastro')
    var_filme = filme(nome, genero, diretor, ano)
    if verificarro(lista, var_filme) == False:
        lista.append(filme(nome, genero, diretor, ano))
    
    return render_template('index.html',lista=lista)

@app.route('/verificar',methods=['POST',])
def verificar():
    senha = request.form['senha']
    nome = request.form['nome']
    if senha == 'senha' and nome == 'fabricio':
        session['usuario_logado'] = nome
        return redirect('/cadastro')
    else:
        return redirect('/login')

@app.route('/cadastro')
def cadastrar():
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect('/login')
    else:
        return render_template('cadastro_filme.html')
    
@app.route('/login')
def paglogar():
    return render_template('login.html')

@app.route('/logout')
def logout():
    session['usuario_logado'] = None
    return redirect('/inicio')

app.run(debug=True)