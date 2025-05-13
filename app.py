from flask import Flask, render_template,jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return render_template("stream.html")

@app.route("/chat", methods=['POST'])
def chat():
    input = request.json.get("message")
    print(input)
    output = input[::-1]

    return jsonify({"message" :output})

if __name__ == "__main__":
    app.run(debug=True)
