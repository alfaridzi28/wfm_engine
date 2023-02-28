from fastapi import APIRouter , Request
from app.config import loop, KAFKA_BOOTSTRAP_SERVERS, KAFKA_TOPIC
from aiokafka import AIOKafkaConsumer, AIOKafkaProducer
import xmltodict

route = APIRouter()

@route.post("/wfmintegration")
async def send(message:Request):

    body = await message.body()
    xml_siteid=xmltodict.parse(body)
    json_key_siteid = xml_siteid['soapenv:Envelope']['soapenv:Body']['wfm:InstallRequest']['wfm:WOHeader']['wfm:WFMSITEID']
    key = json_key_siteid.encode()
    partition = {
        "REG-1" : 0,
        "REG-2" : 1,
        "REG-3" : 2,
        "REG-4" : 3,
        "REG-5" : 4,
        "REG-6" : 5,
        "REG-7" : 6,
    }
    producer = AIOKafkaProducer(loop=loop, bootstrap_servers=KAFKA_BOOTSTRAP_SERVERS)
    await producer.start()
    try: 
        print (f"Sending message with value: {body}")
        await producer.send_and_wait(topic=KAFKA_TOPIC, key=key, value=body, partition=partition[json_key_siteid])
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
