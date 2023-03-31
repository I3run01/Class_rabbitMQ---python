import pika
from pika.exchange_type import ExchangeType

#Start -> Open conection
connection_parameters = pika.ConnectionParameters('localhost')
connection = pika.BlockingConnection(connection_parameters)
channel = connection.channel()
#Finish the open conection step

#Exchange decalres
channel.exchange_declare(exchange='myTopicExchange', exchange_type=ExchangeType.topic)
#Exchange decalres

#Mensage and bind
userPaymentMessage = 'A european user paid for something'
channel.basic_publish(exchange='myTopicExchange', 
                      routing_key='user.europe.payments', body=userPaymentMessage)
print(f"sent message: {userPaymentMessage}")
#Mensage and bind

#Mensage and bind
businessOrderMessage = 'A european ordered goods'
channel.basic_publish(exchange='myTopicExchange', 
                      routing_key='business.europe.order', body=businessOrderMessage)
print(f"sent message: {businessOrderMessage}")
#Mensage and bin

connection.close()