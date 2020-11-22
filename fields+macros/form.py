from wtforms import Form
from wtforms import StringField,TextAreaField
from wtforms.fields.html5 import EmailField



class ComentsForm(Form):
    username = StringField('username')
    email = EmailField('email')
    comment = TextAreaField('comments')
