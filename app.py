# app.py
from flask import Flask, render_template, redirect, url_for, flash, request
from config import Config
from models import db, User,Product,Category, Carrito,bcrypt
from forms import RegistrationForm, LoginForm
from flask_login import LoginManager, login_user, current_user, logout_user, login_required
import email_validator
from productos import load_products
app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)
bcrypt.init_app(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.before_request
def create_tables():
    db.create_all()
    existing_data = db.session.query(Product).first()

    if not existing_data:

            new_user = User(username="admin", email="admin@admin.com", password="")

            new_user.set_password("admin")  

            db.session.add(new_user)

            load_products()

            db.session.commit()
      

@app.route('/')
def index():
    try:
        global user
        userid=user.id
    except:
        userid=0
    conn = db.engine.connect()

    productos = db.session.query(Product).all()  
    db.session.close() 

    conn.close()
    productos1 = productos[:6]
    productos2 = productos[7:13]
    return render_template('index.html',productos1=productos1,productos2=productos2,userid=userid)
@app.route('/register', methods=['GET', 'POST'])
def register():
    global user
    
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('cuenta creada con exito ;)')
        return redirect(url_for('login'))
    return render_template('register.html', form=form,user=user)

@app.route('/login', methods=['GET', 'POST'])
def login():
    global user
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('index'))
        else:
            flash('algo salio mal')
    return render_template('login.html', form=form)

@app.route('/logout')
def logout():
    global user
    user = 0
    logout_user()
    return redirect(url_for('index'))

@app.route('/products')
def products():
    conn = db.engine.connect()

    productos = db.session.query(Product).all()  
    db.session.close() 
    
    conn.close()
    return render_template('products.html',productos=productos)
@app.route('/cafes')
def cafes():
    conn = db.engine.connect()

    productos = db.session.query(Product).filter_by(category="Café").all()
    db.session.close()

    conn.close()
    return render_template('cafes.html', productos=productos)
@app.route('/camisas')
def camisas():
    conn = db.engine.connect()

    productos = db.session.query(Product).filter_by(category="Camisa").all()
    db.session.close()

    conn.close()
    return render_template('camisas.html', productos=productos)
@app.route('/tazas')
def tazas():
    conn = db.engine.connect()

    productos = db.session.query(Product).filter_by(category="Taza").all()
    db.session.close()

    conn.close()
    return render_template('tazas.html', productos=productos)
@app.route('/cafeteras')
def cafeteras():
    conn = db.engine.connect()

    productos = db.session.query(Product).filter_by(category="Cafetera").all()
    db.session.close()

    conn.close()
    return render_template('cafeteras.html', productos=productos)
@app.route('/te')
def te():
    conn = db.engine.connect()

    productos = db.session.query(Product).filter_by(category="Té").all()
    db.session.close()

    conn.close()
    return render_template('te.html', productos=productos)
@app.route('/misc')
def misc():
    conn = db.engine.connect()

    productos = db.session.query(Product).filter_by(category="Misc").all()
    db.session.close()

    conn.close()
    return render_template('misc.html', productos=productos)

@app.route('/register_product',methods=['GET', 'POST'])
def reg_products():
    global user
    try:
        if user.id==1:
            if request.method == 'POST':
                    name = request.form['name']
                    price = float(request.form['price'])
                    description = request.form['description']
                    category = request.form['category']
                    image_url = request.form['image_url']

                    # Create a new product object
                    new_product = Product(name=name, price=price, desc=description, category=category, image_url=image_url)

                    # Add product to database session
                    db.session.add(new_product)
                    db.session.commit()
            conn = db.engine.connect()

            cats = db.session.query(Category).all()  # Fetch all products
            db.session.close()  # Close session

            conn.close()
            return render_template('register_product.html',cats=cats)
        else:
            return redirect('/')
    except:
        return redirect('/')


# @login_required
@app.route('/carrito')
@login_required
def carrito():
    try:
        carrito_productos = Carrito.query.filter_by(usuario_id=current_user.id).all()
        productos_en_carrito = []
        for carrito_producto in carrito_productos:
            producto = Product.query.filter_by(name=carrito_producto.producto_id).first()
            if producto:
                productos_en_carrito.append(producto)
        return render_template('carrito.html', productos_en_carrito=productos_en_carrito)
    except Exception as e:
        flash('Error al cargar el carrito de compras')
        return redirect(url_for('index'))
    
@app.route('/add_to_cart/<product_name>')
@login_required
def add_to_cart(product_name):
    try:
        # Verificar si el producto ya está en el carrito del usuario
        carrito_producto = Carrito.query.filter_by(usuario_id=current_user.id, producto_id=product_name).first()
        if carrito_producto:
            flash('El producto ya está en tu carrito.')
        else:
            nuevo_carrito_producto = Carrito(producto_id=product_name, usuario_id=current_user.id)
            db.session.add(nuevo_carrito_producto)
            db.session.commit()
            flash('Producto añadido al carrito exitosamente.')
    except Exception as e:
        flash('Hubo un error al añadir el producto al carrito.')
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)
