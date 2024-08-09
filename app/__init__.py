from flask import Flask, request, jsonify, redirect 
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os
import json

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config.Config')
    db.init_app(app)
    migrate.init_app(app, db)

    @app.route('/usuarios')
    def oque_eu_quiser():
        usuarios = models.User.query.all()
        html = '''
            <!DOCTYPE html>
            <html lang="pt-BR">
            <head>
                <meta charset="UTF-8">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <title>Lista de Usuários</title>
                <style>
                    body {
                        font-family: Arial, sans-serif;
                        margin: 20px;
                        padding: 0;
                        background-color: #f4f4f4;
                    }
                    .container {
                        max-width: 800px;
                        margin: auto;
                        background: #fff;
                        padding: 20px;
                        border-radius: 8px;
                        box-shadow: 0 0 10px rgba(0,0,0,0.1);
                    }
                    h1 {
                        text-align: center;
                        color: #333;
                    }
                    ul {
                        list-style-type: none;
                        padding: 0;
                    }
                    li {
                        margin-bottom: 10px;
                        padding: 15px;
                        background: #f9f9f9;
                        border-radius: 4px;
                        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
                    }
                    li:hover {
                        background: #e9e9e9;
                    }
                    .cpf {
                        font-size: 0.8em;
                        color: #666;
                    }
                </style>
            </head>
            <body>
                <div class="container">
                    <h1>Lista de Usuários</h1>
                    <ul>
        '''

        for usuario in usuarios:
            html += f'''
                <li>
                    <strong>{usuario.nome}</strong>
                    <span class="cpf">CPF: {usuario.cpf}</span>
                    <div class="actions">
                        <a href="/edit/{usuario.id}">Editar</a>
                    </div>
                </li>
            '''

        html += '''
                    </ul>
                </div>
            </body>
            </html>
        '''

        return html

    @app.route('/register', methods=['POST'])
    def registro():
        nome_pessoa = request.form['nome']
        cpf_pessoa = request.form['cpf']

        usuario = models.User(nome=nome_pessoa, cpf=cpf_pessoa)
        db.session.add(usuario)
        db.session.commit()
        return "Os dados foram salvos e o nome enviado é: " + nome_pessoa + " e o cpf é: " + cpf_pessoa

    @app.route('/edit/<int:id>', methods=['GET', 'POST'])
    def edit_user(id):
        usuario = models.User.query.get_or_404(id)
        
        if request.method == 'POST':
            usuario.nome = request.form['nome']
            usuario.cpf = request.form['cpf']
            db.session.commit()
            return redirect('/usuarios')

        return '''
            <!DOCTYPE html>
            <html lang="pt-BR">
            <head>
                <meta charset="UTF-8">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <title>Editar Usuário</title>
            </head>
            <body>
                <h2>Editar Usuário</h2>
                <form action="/edit/{id}" method="post">
                    <label for="nome">Nome:</label><br>
                    <input type="text" id="nome" name="nome" value="{nome}" required><br><br>
                    
                    <label for="cpf">CPF:</label><br>
                    <input type="text" id="cpf" name="cpf" value="{cpf}" placeholder="000.000.000-00" required><br><br>
                    
                    <input type="submit" value="Salvar">
                </form>
                <a href="/usuarios">Voltar para a lista de usuários</a>
            </body>
            </html>
        '''.format(id=usuario.id, nome=usuario.nome, cpf=usuario.cpf)

    @app.route('/delete/<int:id>', methods=['POST'])
    def delete_user(id):
        usuario = models.User.query.get_or_404(id)
        db.session.delete(usuario)
        db.session.commit()
        return redirect('/usuarios')


    @app.route("/")
    def pagina_inicial():
        return '''<!DOCTYPE html>
            <html lang="pt-br">
            <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Formulário de Cadastro</title>
            </head>
            <body>
                <h2>Formulário de Cadastro</h2>
                <form action="/register" method="post">
                    <label for="nome">Nome:</label><br>
                    <input type="text" id="nome" name="nome" required><br><br>
                    
                    <label for="cpf">CPF DA PESSOA:</label><br>
                    <input type="text" id="cpf" name="cpf" placeholder="000.000.000-00" required><br><br>
                    
                    <input type="submit" value="Enviar">
                </form>
            </body>
            </html>'''


    with app.app_context():
        from . import models
    return app