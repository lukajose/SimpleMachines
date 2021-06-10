from kafka import KafkaConsumer
import json


def json_deserializer(v):
    if v is None: return
    try:
        return json.loads(v.decode('utf-8'))
    except json.decoder.JSONDecodeError:
        print("Unable to deserialize json")
        return None


consumer = KafkaConsumer('pageview', bootstrap_servers=['localhost:9092'],value_deserializer=json_deserializer)
for message in consumer:
    print("========= New Message =============")
    print (message.value)