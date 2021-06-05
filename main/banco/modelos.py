from ..db import db
import flask_bcrypt


class Treinadores(db.Document):
    usuario = db.StringField(required=True, unique=True)
    nome = db.StringField(required=True)
    sobrenome = db.StringField(required=True)
    dtnascimento = db.DateTimeField(required=True)
    senha_hash = db.StringField(required=True)

    @property
    def senha(self):
        raise AttributeError('senha: campo somente para armazenamento')

    @senha.setter
    def senha(self, senha):
        self.senha_hash = flask_bcrypt.generate_password_hash(senha).decode('utf-8')

    def checar_senha(self, senha):
        return flask_bcrypt.check_password_hash(self.senha_hash, senha)

    def __repr__(self):
        return "<User '{}'>".format(self.usuario)