import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')


import django
django.setup()


from products.models import Product, Brand, Category
import random
from faker import Faker

def seed_category(n):
    fake = Faker()
    images = ['bakery.png','Dairy.png','meat.png','sea.png','Vegetables.png']
    for _ in range(n):
        name = fake.name()
        image = f"category/{images[random.randint(0,4)]}"
        Category.objects.create(
            name=name,      
            image=image,
        )
    print(f'Successfully Seeded {n} Category')






def seed_brand(n):
    fake = Faker()
    images = ['Almarai.png','americana.png','bake.png','Egyptian_Fresh.png','farm.png','Green_Valley.png','Lactel.png','simpex.png']
    for _ in range(n):
        name = fake.name()
        image = f"brands/{images[random.randint(0,7)]}"
        Brand.objects.create(
            name=name,      
            image=image,
            category = Category.objects.get(id=random.randint(2,16))  # Randomly assign a category

        )
    print(f'Successfully Seeded {n} Category')


def seed_product(n):
    fake = Faker()
    images = ['bread1.png','bread2.png','meat.png','meat1.png','meat2.png','potato.png','potato2.png','potato3.png','sea1.png','zabady.png']
    flag_type = ['New', 'Feature', 'Sale']
    for _ in range(n):
        name = fake.name()
        subtitle = fake.text(max_nb_chars=500)
        skl = random.randint(1000, 100000)
        descrabtion = fake.text(max_nb_chars=2000)
        price = round(random.uniform(20.99, 500.99),2)
        image = f"products/{images[random.randint(0,9)]}"
        flag = flag_type[random.randint(0,2)]
        quantity = random.randint(1, 100)


        Product.objects.create(
            name=name,      
            subtitle=subtitle,
            skl=skl,
            desc=descrabtion,
            price=price,
            image=image,
            flag=flag,
            quantity=quantity,
            brand = Brand.objects.get(id=random.randint(1,21)),
            category = Category.objects.get(id=random.randint(2,16)),  # Randomly assign a category

        )
    print(f'Successfully Seeded {n} Product')






#seed_category(5)  # Create 10 categories
#seed_brand(10)    # Create 10 brands            
seed_product(100)  # Create 100 products