from flask import Flask, jsonify

app = Flask(__name__)


@app.get("/")
def index():
    return jsonify(message="SERVICERUNNING", port=8000)


@app.get("/health")
def health():
    return jsonify(status="ok")


if __name__ == "__main__":
    print("SERVICERUNNING on port 8000", flush=True)
    app.run(host="0.0.0.0", port=8000)
