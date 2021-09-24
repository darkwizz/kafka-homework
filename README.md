# Kafka homework repository

To run the producer:
```bash
$ cd producer  # otherwise schema/create-user-request.avsc will not be found
$ python main.py [-h, --help] [--topic TOPIC] [--bootstrap-servers BOOTSTRAP_SERVERS] [--schema-registry SCHEMA_REGISTRY] [--schema-file SCHEMA_FILE]
```

Default values of the parameters:

```
topic - user-test-2
bootstrap-servers - localhost:9092
schema-registry - http://localhost:8081
schema-files - create-user-request.avsc
```