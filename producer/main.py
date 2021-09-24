from argparse import ArgumentParser

from entities.user import User
from generator.user_generator import generate_users
from producer.user_producer import UserProducer


def parse_command_line_args():
    parser = ArgumentParser()
    parser.add_argument('--topic', required=False, default='user-test-2', help='Topic name')
    parser.add_argument('--bootstrap-servers', required=False, default='localhost:9092',
                        help='Bootstrap server address')
    parser.add_argument('--schema-registry', required=False, default='http://localhost:8081',
                        help='Schema Registry url')
    parser.add_argument('--schema-file', required=False, default='create-user-request.avsc',
                        help='File name of the Avro schema to use')
    return parser.parse_args()


if __name__ == '__main__':
    args = parse_command_line_args()
    user_producer = UserProducer(args)
    for users in generate_users():
        user_producer.send_records(users)
