from . import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(120), nullable=False)
    cpf = db.Column(db.String(15), nullable=False, unique=True)

    def __repr__(self):
        return f'<User {self.nome}>'

class Escola(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(255), nullable=False)
    data_fundacao = db.Column(db.DateTime(), nullable=False)
    telefone = db.Column(db.String(14), nullable=True)
