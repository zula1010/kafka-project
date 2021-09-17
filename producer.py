from kafka import KafkaProducer

from kafka_func import TOPIC_NAME, KAFKA_SERVER, encode


producer = KafkaProducer(bootstrap_servers=KAFKA_SERVER)
file = open('data.json', 'r')
lines = file.readlines()
counter = 0
for line in lines:
	producer.send(TOPIC_NAME, encode(line))
	counter += 1
	print(f'Message No: {counter} sent!')
producer.flush()
