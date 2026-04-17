from flask import Flask, request, jsonify, render_template
from db import init_db, add_message, get_messages

app = Flask(__name__)

init_db()

@app.route("/")
def home():
    messages = get_messages()
    return render_template("index.html", messages=messages)

@app.route("/add", methods=["POST"])
def add():
    text = request.form.get("text")
    add_message(text)
    return jsonify({"status": "saved", "text": text})

@app.route("/api/messages")
def api_messages():
    return jsonify(get_messages())

@app.route("/health")
def health():
    return {"status": "UP"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
