from kafka import KafkaConsumer, KafkaProducer
import os
import json
import uuid
from concurrent.futures import ThreadPoolExecutor

TOPIC_NAME = "deltas"

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

def sidewalksProcessFunction(data):
    print(data)

for sidewalk in consumer:
    sidewalk_data = sidewalk.value
    sidewalksProcessFunction(sidewalk_data)
