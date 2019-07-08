import paho.mqtt.client as mqtt

def on_connect(client, userdata, flags, rc):
    client.subscribe("result") 
#topic here as "result"

def on_message(client, userdata, msg):
    print(msg.topic+" -  "+str(msg.payload))

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

#client.username_pw_set("USUARIO", password="SENHA")

client.connect("192.168.0.***", 1883, 60)


client.loop_forever()
