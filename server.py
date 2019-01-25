from flask import (Flask, render_template, request, Response)
import network
app = Flask(__name__)


@app.route("/")
def index():
    return render_template('index.html')


@app.route("/send_image", methods=["POST"])
def image_vector():
    return Response(response="1", status=201)

