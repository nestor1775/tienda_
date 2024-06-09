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



class Product(db.Model):

    name = db.Column(db.String(255), primary_key=True)
    price = db.Column(db.Float, nullable=False)
    desc = db.Column(db.String(255), primary_key=True)
    category = db.Column(db.String(30), primary_key=True)
    image_url = db.Column(db.String(255))  


    def __repr__(self):
        return f"<Product(id={self.id}, name='{self.name}', price={self.price}, stock={self.stock}, image_url='{self.image_url}')>"

class Category(db.Model):

    name = db.Column(db.String(255), primary_key=True)
    def __repr__(self):
        return f"name='{self.name}'"

class Carrito(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    producto_id = db.Column(db.String(255), db.ForeignKey('product.name'), nullable=False)
    usuario_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    producto = db.relationship('Product', backref='carrito_productos')
    usuario = db.relationship('User', backref='carrito_usuarios')

    def __repr__(self):
        return f"<Carrito(id={self.id}, producto_id='{self.producto_id}', usuario_id='{self.usuario_id}')>"
