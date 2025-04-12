from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/')
def home():
    return "Virtual Study Buddy is running!"

if __name__ == '__main__':
    app.run(debug=True)
