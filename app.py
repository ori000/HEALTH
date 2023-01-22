from flask import Flask, render_template, request, jsonify
from chatbot import chatbot

app=Flask(__name__)


@app.route("/", methods=["GET"])
def index_get():
    return render_template("base.html")

@app.route("/predict", methods=["POST"])
def predict():
    text =request.get_json().get("message")

    # to do: check if text is valid

    response=chatbot(text)
    message={"answer": response}

    return jsonify(message)
    
if __name__=="__main__":
    app.run(debug=True)
    
