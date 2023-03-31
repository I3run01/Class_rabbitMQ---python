import pika
from pika.exchange_type import ExchangeType

#Start -> Open conection
connection_parameters = pika.ConnectionParameters('localhost')

connection = pika.BlockingConnection(connection_parameters)

channel = connection.channel()
#Finish the open conection step

channel.exchange_declare(exchange='routing', exchange_type=ExchangeType.direct) #type of your exchange

message = f"This message needs to be rouring" #message itself

channel.basic_publish(exchange='routing', routing_key='both', body=message) #message publishing

print(f"sent message: {message}") #the message in console

connection.close()