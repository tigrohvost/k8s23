from flask import Flask
import random

app = Flask(__name__)

@app.route('/')
def home():
	return "It's alive! =^_____^="

@app.route('/random', methods=['GET'])
def get_random():
      return str(random.randint(1,1000))

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
