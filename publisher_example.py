import paho.mqtt.publish as publish

publish.single("result", "Hello World", hostname="192.168.0.101")
