from flask import Flask, request, jsonify

app = Flask(__name__)

VERSION = "1.1.0"


@app.route("/health", methods=["GET"])
def health():
    return jsonify({
        "status": "healthy",
        "application": "student-ml-api",
        "version": VERSION,
        "model_version": "model-1"

    })


@app.route("/predict", methods=["POST"])
def predict():

    data = request.get_json()

    if not data or "value" not in data:
        return jsonify({
            "error": "Missing value"
        }), 400

    value = data["value"]

    if not isinstance(value, (int, float)) or isinstance(value, bool):
        return jsonify({
            "error": "value must be a number"
        }), 400

    prediction = value * 2

    return jsonify({
        "input": value,
        "prediction": prediction
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)