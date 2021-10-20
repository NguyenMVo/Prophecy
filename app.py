from flask import Flask, render_template, request
import ocr
import translator

app = Flask(__name__)

@app.route("/", methods=["GET"])
def hello_world():
    return render_template("index.html")

@app.route("/predict", methods=["GET", "POST"])
def predict():
    url_text = request.form["textsend"]
    org_text = ocr.detection(url_text)
    sentence = translator.translate(org_text)
    return render_template("index.html", prediction= sentence)

if __name__ == "__main__":
    app.run(port=8000, debug=True)
