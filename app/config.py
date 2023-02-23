import asyncio

# env variable
# KAFKA_BOOTSTRAP_SERVERS = "localhost:9093"
KAFKA_BOOTSTRAP_SERVERS = "10.62.61.102:19092"
# KAFKA_TOPIC = "kafka"
KAFKA_TOPIC = "WFM_OSM"
loop = asyncio.get_event_loop()
