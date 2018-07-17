import requests
from flask import Flask, render_template

app = Flask(__name__)

def get_temperature():
  resp = requests.get(
      'https://api.darksky.net/forecast/cc451c6cb0b74ab2606660e8ffc3ec29/37.8267,-122.4233')
  temperature = resp.json()['currently']['temperature']
  return temperature

@app.route('/')
def index():
  temp = get_temperature()
  return render_template('template/index.html', temp = temp)

if __name__ == '__main__':
  app.run(debug=True)
