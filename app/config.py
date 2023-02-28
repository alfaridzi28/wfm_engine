import asyncio

# env variable
KAFKA_BOOTSTRAP_SERVERS = "10.62.61.102:19092"
KAFKA_TOPIC = "WFM_OSM_IN"
loop = asyncio.get_event_loop()
