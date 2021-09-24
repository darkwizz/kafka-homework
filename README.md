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

## Use kafka deployed in docker (cheatsheet)

#### Where to get the `docker-compose.yml`
```
$ curl --silent --output docker-compose.yml https://raw.githubusercontent.com/confluentinc/cp-all-in-one/6.2.1-post/cp-all-in-one/docker-compose.yml
$ docker-compose up
```

#### Create topic:
```bash
$ docker-compose exec broker kafka-topics --create --zookeeper \ zookeeper:2181 --replication-factor 1 --partitions 1 --topic <topic_name>
```