import requests
from flask import Flask

app = Flask(__name__)

def get_temperature():
  resp = requests.get('https://api.darksky.net/forecast/cc451c6cb0b74ab2606660e8ffc3ec29/37.8267,-122.4233')
  temperature = resp.json()['currently']['temperature']
  print (temperature)
  return temperature

@app.route('/')
def index():
  temp = get_temperature()
  return str(temp)

if __name__ == '__main__':
  app.run()
