from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return "Docker is running on AWS EC2 🚀"

app.run(host='0.0.0.0', port=5000)
