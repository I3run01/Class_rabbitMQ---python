import pika
from pika.exchange_type import ExchangeType

def on_message_received(ch, method, properties, body): #function that received the queue
        print(f'firstConsumer received new message: {body}')

#Start -> Open conection
connection_parameters = pika.ConnectionParameters('localhost')

connection = pika.BlockingConnection(connection_parameters)

channel = connection.channel()
#Finish the open conection step

channel.exchange_declare(exchange='pubsub', exchange_type=ExchangeType.fanout) #type of your exchange

queue = channel.queue_declare(queue='', exclusive=True)

channel.queue_bind(exchange='pubsub', queue=queue.method.queue)

channel.basic_consume(queue=queue.method.queue,on_message_callback=on_message_received) #which function goes for each queue

print('Starting consuming')
 
channel.start_consuming() #start