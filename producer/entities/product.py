from faker import Faker
from faker.providers import company, barcode


class Product:
    def __init__(self, name, barcode, category, price, manufacturer, unit_quantity):
        self.name = name
        self.barcode = barcode
        self.category = category
        self.price = price
        self.manufacturer = manufacturer
        self.unit_quantity = unit_quantity
    
    def to_json(self):
        return self.__dict__
    
    @staticmethod
    def generate_random_product():
        fake = Faker()
        fake.add_provider(company)
        fake.add_provider(barcode)

        return Product(
            name=fake.sentence(nb_words=5, variable_nb_words=True),
            barcode=fake.ean(),
            category=fake.word(),
            price=fake.pyfloat(right_digits=2, positive=True, max_value=5000),
            manufacturer=fake.company(),
            unit_quantity=fake.pyint(min_value=1, max_value=100, step=1)
        )