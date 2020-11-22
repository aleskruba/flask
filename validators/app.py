from flask import Flask,render_template,request

from form import ComentsForm

app = Flask(__name__)


@app.route('/',methods = ['GET','POST'])
def index():
    comment_form = ComentsForm(request.form)
    if request.method == 'POST' and comment_form.validate():
        print(comment_form.username.data)
        print(comment_form.email.data)
        print(comment_form.comment.data)
    else:
        print("An error in Formular")

    title = "Macros and Fields"
    return render_template('index1.html',title=title,form=comment_form)


if __name__==("__main__"):
    app.run(port=5001)