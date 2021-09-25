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

### Where to get the `docker-compose.yml`:
```
$ curl --silent --output docker-compose.yml https://raw.githubusercontent.com/confluentinc/cp-all-in-one/6.2.1-post/cp-all-in-one-community/docker-compose.yml
$ docker-compose up -d  # to avoid holding stdin by the containers
```

### Create a topic:
```bash
# assuming zookeeper is running in a default zookeeper container (described in the docker-compose.yml)
$ docker-compose exec broker kafka-topics --create --zookeeper zookeeper:2181 --replication-factor 1 --partitions 1 --topic <topic_name>
```

### List topics:
```bash
# assuming zookeeper is running in a default zookeeper container (described in the docker-compose.yml)
$ docker-compose exec broker kafka-topics --list --zookeeper zookeeper:2181
```

### Use console consumer/producer:
```bash
# assuming the containers have the default names
$ docker exec -it broker sh
$> kafka-console-producer --topic <topic> --bootstrap-server <broker>  # localhost:9092
# OR
$> kafka-console-consumer --topic <topic> --bootstrap-server <broker>  # localhost:9092 --from-beginning
```
#### Or if to use *avro* consumer/producer:
```bash
# assuming the containers have the default names
$ docker exec -it schema-registry sh
$> kafka-avro-console-producer ...
$> kafka-avro-console-consumer ...
```

### Connect to KSQL Server using KSQL CLI:
```bash
# assuming the containers have the default names
$ docker exec -it ksqldb-cli sh
$> ksql http://ksqldb-server:8088  # docker-compose exec ksqldb-cli http://ksqldb-server:8088 does not enter anywhere
```


## KSQL Cheatsheet

### Show streams:
```sql
SHOW STREAMS;
```

### Show tables:
```sql
SHOW TABLES;
```

### Drop a stream:
```sql
DROP STREAM <stream-name>;
```

### Execute a script file:
```bash
# assuming the containers have the default names
$ docker exec -it ksqldb-cli sh
$> ksql -f <ksql_script_file>
```


## Work with connectors in containers (cheatsheet)
### Create a connector:
```bash
$ curl -X POST -H "Content-Type: application/json" -d @connector-init/file-connector-sink.json localhost:8083/connectors
```

> For a file connector specified paths will be prepared in the container with the connector server

Connectors [REST API](https://docs.confluent.io/platform/current/connect/references/restapi.html)