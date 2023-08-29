from flask import Flask
from flask_cors import CORS, cross_origin
from flask import request

import random

app = Flask(__name__)
cors = CORS(app)


@app.route("/test")
@cross_origin()
def test():
    return str(random.randint(0, 100))


@app.route("/subscribe", methods=['POST'])
@cross_origin()
def subscribe():
    if request.method == 'POST':
        print(

            "recieved email:",
            request.get_json()["email"]
        )
        return "1"


@app.route("/subscribe", methods=['GET'])
@cross_origin()
def get_prompt():
    if request.method == 'GET':
        print(

            "recieved GET request with prompt:",
            request.get_json()["code"]
        )
        return "<sample code (not implemented)>"


if __name__ == "__main__":
    app.run(debug=True, port=8080)
