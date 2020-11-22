from flask import Flask,render_template

from form import ComentsForm

app = Flask(__name__)


@app.route('/')
def index():
    comment_form = ComentsForm()
    title = "Mascros and Fields"
    return render_template('index1.html',title=title,form=comment_form)


if __name__==("__main__"):
    app.run(port=5001)