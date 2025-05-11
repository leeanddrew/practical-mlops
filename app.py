from flask import Flask, request, jsonify
from hello import hello

app = Flask(__name__)

@app.route("/hello", methods=["POST"])
def run_hello():
    name = request.json.get("name", "world")
    return jsonify({"message": hello(name)})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)