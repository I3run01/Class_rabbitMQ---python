import pika
import time
import random

connection_parameters = pika.ConnectionParameters('localhost')

connection = pika.BlockingConnection(connection_parameters)

channel = connection.channel()

channel.queue_declare(queue='letterbox')

messageID = 1

while (True):
    message = f"Sending message: {messageID}"

    channel.basic_publish(exchange='', routing_key='letterbox', body=message)

    print(f"sent message: {message}")

    time.sleep(random.randint(1, 4))

    messageID += 1