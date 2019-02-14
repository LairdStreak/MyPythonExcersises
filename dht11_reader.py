import dht
import machine
import time
import wifi_connect
import ujson
import urequests

def main():
    while True:
        read()         
        time.sleep(40)

def read():
    d = dht.DHT11(machine.Pin(16))
    d.measure()
    temp = d.temperature()
    humid = d.humidity()
    dict = {}
    dict["temp"] = str(temp)
    dict["humidity"] = str(humid)
    encoded = ujson.dumps(dict)
    print(encoded)
    post_data(encoded)


def post_data(ndata):
    print(ndata)
    wifi_connect.connect()
    headers={'Content-Type': 'application/json'}
    response = urequests.post("https://repl.it/@LairdStreak93/ImpoliteLowLifecycles/dhtdatapush",headers=headers, json=str(ndata))
    print(response.json())