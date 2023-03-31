import pika
import time
import random

def on_message_received(ch, method, properties, body): #function that received the queue
        process_time = random.randint(1, 6)
        print(f'received: {body}, will take {process_time} to process')
        time.sleep(process_time)
        ch.basic_ack(delivery_tag=method.delivery_tag)
        print("Finished prodessing the message")

#Start -> Open conection
connection_parameters = pika.ConnectionParameters('localhost')

connection = pika.BlockingConnection(connection_parameters)

channel = connection.channel()

channel.queue_declare(queue='letterbox')
#Finish the open conection step

channel.basic_qos(prefetch_count=1) # limit the number of unacknowledged messages 

channel.basic_consume(queue='letterbox',on_message_callback=on_message_received) #which function goes for each queue

print('Starting consuming')
 
channel.start_consuming() #start