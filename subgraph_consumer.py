from kafka import KafkaConsumer, KafkaProducer
import os
import json
import uuid
from concurrent.futures import ThreadPoolExecutor

from OSWValidation.validate_json_schema import validate_json_schema

TOPIC_NAME = "subgraphs"

KAFKA_SERVER = "localhost:9092"

consumer = KafkaConsumer(
    TOPIC_NAME,
    auto_offset_reset='earliest',
    value_deserializer=lambda m: json.loads(m.decode('utf-8'))
)

producer = KafkaProducer(
    bootstrap_servers=KAFKA_SERVER,
    api_version=(0, 11, 15)
)

def validateSchema(data):
    schema_path = './OSWValidation/Json Schema/Nodes_schema.json'
    with open(schema_path) as fp:
        schema = json.load(fp)

    print(validate_json_schema(data, schema))

def sidewalksProcessFunction(data):
    validateSchema(data)
    features = data['features']
    num_features = 0
    for feature in features:
        json_payload = json.dumps(feature)
        json_payload = str.encode(json_payload)
        print(json_payload)
        producer.send('deltas', json_payload)
        producer.flush()
        num_features += 1
    print('Sent ' + str(num_features) + ' deltas')

for sidewalk in consumer:
    sidewalk_data = sidewalk.value
    sidewalksProcessFunction(sidewalk_data)
