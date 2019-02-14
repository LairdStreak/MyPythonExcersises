import requests
import json

def main():
    dict = {}
    dict["temp"] = 22
    dict["humidity"] = 11
    encoded = json.dumps(dict)
    headers={'Content-Type': 'application/json'}

    response = requests.post("http://127.0.0.1:3000/dhtdatapush", headers=headers, json=encoded)
    print(response.text)


if __name__ == '__main__':
    main()