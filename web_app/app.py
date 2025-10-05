from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({"message": "Hello from CI/CD demo app!"})

@app.route("/add", methods=["POST"])
def add_numbers():
    data = request.json
    try:
        result = data["a"] + data["b"]
        return jsonify({"result": result})
    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)