from flask import Flask
from flask_cors import CORS, cross_origin

import random

app = Flask(__name__)
cors = CORS(app)

@app.route("/test")
@cross_origin()
def hello():
    return str(random.randint(0, 100))

if __name__ == "__main__":
    app.run(debug=True)