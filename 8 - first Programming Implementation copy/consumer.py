import pika
import time
import random

def on_message_received(ch, method, properties, body):
        process_time = random.randint(1, 6)
        print(f'received: {body}, will take {process_time} to process')
        time.sleep(process_time)
        ch.basic_ack(delivery_tag=method.delivery_tag)
        print("Finished prodessing the message")

connection_parameters = pika.ConnectionParameters('localhost')

connection = pika.BlockingConnection(connection_parameters)

channel = connection.channel()

channel.queue_declare(queue='letterbox')

channel.basic_qos(prefetch_count=1)

channel.basic_consume(queue='letterbox',on_message_callback=on_message_received)

print('Starting consuming')

channel.start_consuming()