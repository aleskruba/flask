from flask import Flask,render_template,request
from wtforms import Form
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.fields.html5 import EmailField
from wtforms.validators import Length, InputRequired, Email, ValidationError


app = Flask(__name__)

class ComentsForm(Form):
    username = StringField('username', [InputRequired(),Length(min=4,max=25,message="Enter a valid username") ])
    email = EmailField('email',[InputRequired(),Email(message="Enter a valid username") ])

@app.route('/',methods = ['GET','POST'])
def index():
    comment_form = ComentsForm(request.form)
    if request.method == 'POST' and comment_form.validate():
        print(comment_form.username.data)
        print(comment_form.email.data)

    else:
        print("An error in Formular")

    title = "Macros and Fields"
    return render_template('index.html',title=title,form=comment_form)


if __name__==("__main__"):
    app.run(port=5005)
