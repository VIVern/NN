from flask import (Flask, render_template, request, Response, json)
import network
from traning_data import (save_to_file, upload_training_data)
from network import Network


app = Flask(__name__)


@app.route("/")
def index():
    return render_template('index.html')


@app.route("/predict", methods=["POST"])
def image_vector():
    vectorized_image = request.get_json()
    print(vectorized_image['image'])

    response = app.response_class(
        response=json.dumps({"id": 1}),
        status=200,
        mimetype='application/json'
    )
    return response


@app.route("/train")
def train():
    data = upload_training_data("training_data/", "0")
    print(data)
    nw = Network()
    nw.train_network(data)
    print(nw.make_prediction(data[0]['image']))

    response = app.response_class(
        response=json.dumps({"status": "trained"}),
        status=200,
        mimetype='application/json'
    )

    return response


@app.route("/send_train_data", methods=["POST"])
def train_json():
    json_data = request.get_json()
    print(json_data)

    if save_to_file(json_data) is False:
        response = app.response_class(
            response=json.dumps({"status": "error occurred"}),
            status=409,
            mimetype='application/json'
        )
    else:
        response = app.response_class(
            response=json.dumps({"status": "saved"}),
            status=200,
            mimetype='application/json'
        )

    return response
