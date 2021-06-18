from kafka import KafkaProducer

producer = KafkaProducer()
producer.send('create_invoice', b'Dummy invoice data')
producer.flush()