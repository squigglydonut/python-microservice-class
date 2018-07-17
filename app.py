import requests

def get_temperature():
  resp = requests.get('https://api.darksky.net/forecast/cc451c6cb0b74ab2606660e8ffc3ec29/37.8267,-122.4233')
  temperature = resp.json()['currently']['temperature']
  print (temperature)

get_temperature()
