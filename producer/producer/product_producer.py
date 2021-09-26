from producer.base_producer import BaseProducer


class ProductProducer(BaseProducer):
    def __init__(self, config_args):
        super().__init__(config_args)
    
    def send_record(self, key, value):
        try:
            self.producer.produce(topic=self.topic, key=key, value=value)
        except Exception as e:
            print(f'Exception while producing record value - {value} to topic - {self.topic}: {e}')
        else:
            print(f'Successfully producing record value - {value} to topic - {self.topic}')
    
    def send_records(self, products):
        for product in products:
            self.send_record(key=product.barcode, value=product.to_json())
        self.producer.flush()