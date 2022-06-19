# performing flask imports
from flask import Flask, jsonify, request
from calculator import result


app = Flask(__name__)  # intance of our flask application

# Route '/' to facilitate get request from our flutter app


@app.route('/calc', methods=['POST'])
def index():
    text = request.values.get('text')
    print(text)
    res = result(text.split())
    print("------------------------------------------")
    return jsonify(res)  # returning key-value pair in json format


if __name__ == "__main__":
    # debug will allow changes without shutting down the server
    app.run(debug=True, port=5000)
