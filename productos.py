from models import db, User,Product,Category, bcrypt
import random
import os
def load_products():
    
    
    def random_img(cat):
        image_folder = f"static/imagenes/{cat}"
        images = [f for f in os.listdir(image_folder) if os.path.isfile(os.path.join(image_folder, f))]
        random_image = random.choice(images)
        image_url=f"imagenes/{cat}/{random_image}"
        return image_url 

    products = [
    {
        "nombre": "Latte",
        "precio": 3.50,
        "descripcion": "Bebida de espresso cremosa con leche vaporizada.",
        "categoria": "Café"
    },
    {
        "nombre": "Espresso Macchiato",
        "precio": 2.75,
        "descripcion": "Un trago de espresso concentrado con una capa de espuma de leche aterciopelada.",
        "categoria": "Café"
    },
    {
        "nombre": "Capuccino",
        "precio": 3.20,
        "descripcion": "Espresso mezclado con leche vaporizada y espuma, creando una bebida rica y cremosa.",
        "categoria": "Café"
    },
    {
        "nombre": "Té verde Sencha",
        "precio": 2.50,
        "descripcion": "Un té verde japonés ligero y refrescante con un sabor vegetal sutil.",
        "categoria": "Té"
    },
    {
        "nombre": "Té negro Earl Grey",
        "precio": 2.80,
        "descripcion": "Un té negro aromático con un toque de bergamota cítrica.",
        "categoria": "Té"
    },
    {
        "nombre": "Smoothie de frutas tropicales",
        "precio": 4.50,
        "descripcion": "Mezcla refrescante de frutas tropicales como mango, piña y fresa.",
        "categoria": "Misc"
    },
    {
        "nombre": "Camisa de franela a cuadros",
        "precio": 25.00,
        "descripcion": "Camisa de franela clásica y cómoda con un patrón a cuadros atemporal.",
        "categoria": "Camisa"
    },
    {
        "nombre": "Camiseta de algodón con estampado gráfico",
        "precio": 15.00,
        "descripcion": "Camiseta suave y transpirable con un diseño gráfico original.",
        "categoria": "Camisa"
    },
    {
        "nombre": "Vestido de verano floral",
        "precio": 30.00,
        "descripcion": "Vestido ligero y fluido con un estampado floral alegre.",
        "categoria": "Misc"
    },
    {
        "nombre": "Cafetera italiana Moka",
        "precio": 20.00,
        "descripcion": "Cafetera clásica para preparar un café espresso fuerte y concentrado en casa.",
        "categoria": "Cafetera"
    },
    {
        "nombre": "Taza de cerámica artesanal",
        "precio": 12.00,
        "descripcion": "Taza única hecha a mano con un diseño artístico.",
        "categoria": "Taza"
    },
    {
        "nombre": "Manta de lana suave",
        "precio": 35.00,
        "descripcion": "Manta acogedora y cálida perfecta para acurrucarse en el sofá.",
        "categoria": "Misc"
    },
        {
        "nombre": "Café Americano",
        "precio": 2.20,
        "descripcion": "Espresso diluido con agua caliente, creando una bebida ligera y robusta.",
        "categoria": "Café"
    },
    {
        "nombre": "Chocolate caliente",
        "precio": 3.00,
        "descripcion": "Bebida cremosa y deliciosa a base de chocolate fundido y leche caliente.",
        "categoria": "Misc"
    },
    {
        "nombre": "Frappuccino",
        "precio": 4.00,
        "descripcion": "Bebida helada a base de café, leche, hielo y crema batida.",
        "categoria": "Café"
    },
    {
        "nombre": "Té de hierbas con menta",
        "precio": 2.30,
        "descripcion": "Infusión refrescante y digestiva a base de hojas de menta.",
        "categoria": "Té"
    },
    {
        "nombre": "Batido de proteínas",
        "precio": 5.50,
        "descripcion": "Bebida nutritiva rica en proteínas, perfecta para después del entrenamiento.",
        "categoria": "Misc"
    },
    {
        "nombre": "Camisa de lino blanca",
        "precio": 32.00,
        "descripcion": "Camisa fresca y transpirable ideal para el verano.",
        "categoria": "Camisa"
    },
    {
        "nombre": "Pantalón vaquero slim fit",
        "precio": 28.00,
        "descripcion": "Pantalón de corte ajustado y moderno para un look casual.",
        "categoria": "Misc"
    },
    {
        "nombre": "Bolso de mano de piel",
        "precio": 65.00,
        "descripcion": "Bolso elegante y duradero hecho de piel auténtica.",
        "categoria": "Misc"
    },
    {
        "nombre": "Molinillo de café eléctrico",
        "precio": 40.00,
        "descripcion": "Dispositivo para moler café fresco en casa.",
        "categoria": "Cafetera"
    },
    {
        "nombre": "Botellín de agua reutilizable",
        "precio": 10.00,
        "descripcion": "Botella ecológica para llevar agua contigo a todas partes.",
        "categoria": "Misc"
    }
]



    for product in products:
        new_product = Product(
        name=product["nombre"],
        price=product["precio"],
        desc=product["descripcion"],
        category=product["categoria"],
        image_url=f"{random_img(product["categoria"])}",)
        db.session.add(new_product)
    categories =[
  "Café",
  "Camisa",
  "Cafetera",
  "Taza",
  "Té",
  "Misc"
]
    for cat in categories:
        new_cat = Category(name=cat)
        db.session.add(new_cat)
            


