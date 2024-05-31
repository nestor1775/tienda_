# models.py
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from flask_bcrypt import Bcrypt

db = SQLAlchemy()
bcrypt = Bcrypt()

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), nullable=False, unique=True)
    email = db.Column(db.String(150), nullable=False, unique=True)
    password = db.Column(db.String(150), nullable=False)

    def set_password(self, password):
        self.password = bcrypt.generate_password_hash(password).decode('utf-8')

    def check_password(self, password):
        return bcrypt.check_password_hash(self.password, password)

class Carritodb(UserMixin,db.Model):
    id = db.Column(db.Integer,primary_key=True)
    idUsuario= db.Column(db.String,nullable=False)
    idProducto = db.Column(db.String,db.ForeignKey('productosdb.ID_PRODUCTO'),nullable=False)
    cantidad = db.Column(db.Float,nullable=False)