import json
from abc import abstractmethod, ABC

from confluent_kafka.avro import AvroProducer

from utils.schema_uploader import load_avro_schema_from_file


class BaseProducer(ABC):
    def __init__(self, config_args):
        self.producer_config = {
            'bootstrap.servers': config_args.bootstrap_servers,
            'schema.registry.url': config_args.schema_registry
        }

        self.topic = config_args.topic

        key_schema, value_schema = load_avro_schema_from_file(config_args.schema_file)
        self.producer = AvroProducer(
            self.producer_config,
            default_key_schema=key_schema,
            default_value_schema=value_schema
        )
    
    @abstractmethod
    def send_record(self, key, value):
        raise NotImplementedError