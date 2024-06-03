from models import db, User,Product,Category, bcrypt
import random
import os
def load_products():
    
    image_folder = 'static/imagenes'
    images = [f for f in os.listdir(image_folder) if os.path.isfile(os.path.join(image_folder, f))]
    def random_img():
        random_image = random.choice(images)
        image_url=f"imagenes/{random_image}"
        return image_url 

    products = [
        {"name": "Latte", "price": 3.50, "description": "Creamy espresso drink with steamed milk.", "category": "Coffee"},
        {"name": "Cappuccino", "price": 3.75, "description": "Espresso, steamed milk, and milk foam.", "category": "Coffee"},
        {"name": "Americano", "price": 3.25, "description": "Espresso diluted with hot water.", "category": "Coffee"},
        {"name": "Mocha", "price": 4.00, "description": "Espresso, chocolate, and steamed milk.", "category": "Coffee"},
        {"name": "Caramel Macchiato", "price": 4.25, "description": "Espresso, vanilla, caramel drizzle, and milk.", "category": "Coffee"},
    ]
    for product in products:
        new_product = Product(
        name=product["name"],
        price=product["price"],
        desc=product["description"],
        category=product["category"],
        image_url=f"{random_img()}",)
        db.session.add(new_product)
        
    categories =[
  "Coarse",
  "Medium-Coarse",
  "Medium",
  "Medium-Fine",
  "Fine",
  "Turkish"
]
    for cat in categories:
        new_cat = Category(name=cat)
        db.session.add(new_cat)
            


