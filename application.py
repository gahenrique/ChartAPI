from flask import Flask, request, make_response, abort
from flask_cors import CORS
from service import Charts

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return "Chart API. Use the endpoint /plot/line or /plot/pie"

@app.route('/plot/line', methods=['POST'])
def plot_api():
    # json {"x": [n], "y": [n], "labels": [n]}

    if not request.json or "x" not in request.json or "y" not in request.json or "labels" not in request.json:
        abort(400)

    x = request.json.get("x")
    y = request.json.get("y")
    labels = request.json.get("labels")

    if len(x) != len(y) or len(x) != len(labels):
        abort(400)

    imgData = Charts.get_chart(x, y, labels)
    response = make_response(imgData)
    response.headers.set('Content-Type', 'image/png')
    return response

@app.route('/plot/pie', methods=['POST'])
def plot_pie():
    # json {"sizes": [n], "labels": [n]}

    if not request.json or "sizes" not in request.json or "labels" not in request.json:
        abort(400)
    
    sizes = request.json.get("sizes")
    labels = request.json.get("labels")

    if len(sizes) != len(labels):
        abort(400)
    
    imgData = Charts.get_pie_chart(sizes, labels)
    response = make_response(imgData)
    response.headers.set('Content-Type', 'image/png')
    return response


if __name__ == "__main__":
    app.run(debug=True, port=8000)