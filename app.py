from app import create_app
app = create_app()

if __name__ == "__main__":
    app.run(debug=True)

# @app.route('/tututubarao')
# def oque_eu_quiser():
#     return "<h5> ALguma coisa</h5>"

# @app.route('/register', methods=['POST'])
# def registro():
#     nome = request.form['nome']
#     cpf = request.form['cpf']
#     return "O nome enviado é: " + nome + " e o cpf é: " + cpf

# @app.route("/")
# def pagina_inicial():
#     return '''<!DOCTYPE html>
#         <html lang="pt-br">
#         <head>
#         <meta charset="UTF-8">
#         <meta name="viewport" content="width=device-width, initial-scale=1.0">
#         <title>Formulário de Cadastro</title>
#         </head>
#         <body>
#             <h2>Formulário de Cadastro</h2>
#             <form action="/register" method="post">
#                 <label for="nome">Nome:</label><br>
#                 <input type="text" id="nome" name="nome" required><br><br>
                
#                 <label for="cpf">CPF DA PESSOA:</label><br>
#                 <input type="text" id="cpf" name="cpf" placeholder="000.000.000-00" required><br><br>
                
#                 <input type="submit" value="Enviar">
#             </form>
#         </body>
#         </html>'''



