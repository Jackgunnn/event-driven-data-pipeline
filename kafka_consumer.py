from kafka import KafkaConsumer
import json

# Consumer:
# Kafka -> bytes -> decode -> string -> loads -> dict   
consumer = KafkaConsumer(
        'discuzz_events', 
        bootstrap_servers='localhost:9092',
        value_deserializer=lambda v: json.loads(v.decode('utf-8')) # bytes -> JSON string -> Python dict
)

for msg in consumer:
    print(msg.value['event_type'])
