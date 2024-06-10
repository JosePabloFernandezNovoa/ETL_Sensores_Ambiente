from json import dumps
from kafka import KafkaProducer
from datetime import datetime 
import time

producer = KafkaProducer(
    value_serializer=lambda msg: dumps(msg).encode("utf-8"),
    bootstrap_servers=["ceserver1:9092","ceserver2:9092","ceserver3:9092"])

producer.send(
    "2024_145_ruido",
    value={str(datetime.now()): str(msg)})

time.sleep(5)
producer.flush()
return msg