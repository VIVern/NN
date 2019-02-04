from flask import (Flask, render_template, request, Response, json)
import network


app = Flask(__name__)


@app.route("/")
def index():
    return render_template('index.html')


@app.route("/send_image", methods=["POST"])
def image_vector():
    vectorized_image = request.get_json()
    print(vectorized_image['image'])


    response = app.response_class(
        response=json.dumps({"id": 1}),
        status=200,
        mimetype='application/json'
    )
    return response

