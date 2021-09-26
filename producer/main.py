from argparse import ArgumentParser

from entities.user import User
from generator.entity_generator import generate_users, generate_products
from producer.user_producer import UserProducer
from producer.product_producer import ProductProducer


def parse_command_line_args():
    parser = ArgumentParser()
    parser.add_argument('--topic', required=False, default='user-test-2', help='Topic name')
    parser.add_argument('--bootstrap-servers', required=False, default='localhost:9092',
                        help='Bootstrap server address')
    parser.add_argument('--schema-registry', required=False, default='http://localhost:8081',
                        help='Schema Registry url')
    parser.add_argument('--schema-file', required=False, default='create-user-request.avsc',
                        help='File name of the Avro schema to use')
    parser.add_argument('-g', '--generator', required=False, default='user', choices=('user', 'product'),
                        help='Entity generator')
    return parser.parse_args()


if __name__ == '__main__':
    args = parse_command_line_args()
    if args.generator == 'user':
        producer = UserProducer(args)
        generator = generate_users
    elif args.generator == 'product':
        producer = ProductProducer(args)
        generator = generate_products
    for entities in generator():
        producer.send_records(entities)
