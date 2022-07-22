from flask import Flask, request
from functions import doCalculate

application = Flask(__name__)

@application.route('/')

@application.route('/', methods=['GET'])
def get():
  return "Hello python"

# Create Item
@application.route('/calculate', methods=['POST'])
def calculate():
  body = request.get_json()
  return doCalculate(body["dimensions"])

if __name__ == '__main__':
  application.run(host='0.0.0.0')