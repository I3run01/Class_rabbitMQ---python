import pika
from pika.exchange_type import ExchangeType

def on_message_received(ch, method, properties, body): #function that received the queue
        print(f'Payments service - received new message: {body}')

#Start -> Open conection
connection_parameters = pika.ConnectionParameters('localhost')

connection = pika.BlockingConnection(connection_parameters)

channel = connection.channel()

channel.exchange_declare(exchange='myTopicExchange', exchange_type=ExchangeType.topic)

queue = channel.queue_declare(queue='', exclusive=True)
#Finish the open conection step

channel.queue_bind(exchange='myTopicExchange', queue=queue.method.queue,
                   routing_key='#.payments')

channel.basic_consume(queue=queue.method.queue, auto_ack=True, on_message_callback=on_message_received) #which function goes for each queue

print('Starting consuming')
 
channel.start_consuming() #start