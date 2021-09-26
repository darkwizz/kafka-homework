import random
from time import sleep

from entities.user import User
from entities.product import Product


def generate_users(batch_num=10, batch_size_from=50, batch_size_to=100):
    for i in range(batch_num):
        users = []
        batch_size = random.randint(batch_size_from, batch_size_to)
        print(f'Batch #{i} size: {batch_size}')
        for _ in range(batch_size):
            users.append(User.generate_random_user())
        yield users
        sleep(5)


def generate_products(batch_num=10, batch_size_from=50, batch_size_to=100):
    for i in range(batch_num):
        batch_size = random.randint(batch_size_from, batch_size_to)
        print(f'Batch #{i} size: {batch_size}')
        products = [Product.generate_random_product() for _ in range(batch_size)]
        yield products
        sleep(5)
