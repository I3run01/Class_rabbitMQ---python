import pika
import time
import random

#Start -> Open conection
connection_parameters = pika.ConnectionParameters('localhost')

connection = pika.BlockingConnection(connection_parameters)

channel = connection.channel()

channel.queue_declare(queue='letterbox')
#Finish the open conection step


messageID = 1 #message id

while (True): #looping
    message = f"Sending message: {messageID}" #message itself

    channel.basic_publish(exchange='', routing_key='letterbox', body=message) #message publishing

    print(f"sent message: {message}") #the message in console

    time.sleep(random.randint(1, 4)) #sleep time

    messageID += 1 #sum 1 in he messaege id