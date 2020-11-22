from flask import Flask,render_template,request
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route('/process',methods=['POST'])
def process():
    name = request.form["name"]
    comment = request.form["comment"]
    posted = datetime.today()
    return render_template("index.html", name=name,comment=comment,posted=posted)


if __name__=="__main__":
    app.run(debug=True, port=7000)
