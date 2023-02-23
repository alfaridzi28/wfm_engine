from fastapi import APIRouter , Request
from config import loop, KAFKA_BOOTSTRAP_SERVERS, KAFKA_TOPIC
from aiokafka import AIOKafkaConsumer, AIOKafkaProducer
import xml.etree.ElementTree as ET


route = APIRouter()

@route.post("/wfmintegration")
async def send(message:Request):

    body = await message.body()
    producer = AIOKafkaProducer(loop=loop, bootstrap_servers=KAFKA_BOOTSTRAP_SERVERS)
    await producer.start()
    try: 
        print (f"Sending message with value: {body}")
        await producer.send_and_wait(topic=KAFKA_TOPIC, value=body)
        return body
    finally:
        await producer.stop()

async def consume():
    consumer = AIOKafkaConsumer(KAFKA_TOPIC, loop=loop, bootstrap_servers=KAFKA_BOOTSTRAP_SERVERS)
    await consumer.start()
    try:
        async for msg in consumer:
            print(f"Consumer msg: {msg}")
    finally:
        await consumer.stop()
