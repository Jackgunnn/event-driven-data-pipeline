from event_simulator import generate_event
from kafka import KafkaProducer, KafkaConsumer
import json


# Producer:
# dict -> dumps -> string -> encode -> bytes -> Kafka
producer = KafkaProducer(
    bootstrap_servers='localhost:9092', 
    value_serializer=lambda v: json.dumps(v).encode('utf-8') # Python dict -> JSON string -> bytes
) 


for i in range(5):
    event = generate_event()
    producer.send('discuzz_events', event)






 