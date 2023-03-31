import pika
from pika.exchange_type import ExchangeType

#Start -> Open conection
connection_parameters = pika.ConnectionParameters('localhost')

connection = pika.BlockingConnection(connection_parameters)

channel = connection.channel()
#Finish the open conection step

#declare your exchange
channel.exchange_declare(exchange='pubsub', exchange_type=ExchangeType.fanout) 

message = f"Hello I want to broadcast this message" #message itself

channel.basic_publish(exchange='pubsub', routing_key='', body=message) #message publishing

print(f"sent message: {message}") #the message in console

connection.close()