from kafka import KafkaConsumer

consumer = KafkaConsumer()
# Topics need to be created before
consumer.subscribe(pattern=".*")

for msg in consumer:
    print (msg)
