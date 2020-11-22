from wtforms import Form
from wtforms import StringField,TextAreaField,SubmitField
from wtforms.fields.html5 import EmailField
from wtforms.validators import  Length,InputRequired,Email,ValidationError

def length_honeypot(form,field):
    if len(field.data) > 0:
        raise ValidationError('This field must be empty')

class ComentsForm(Form):
    username = StringField('username', [InputRequired(),Length(min=4,max=25,message="Enter a valid username") ])
    email = EmailField('email',[InputRequired(),Email(message="Enter a valid username") ])
    comment = TextAreaField('comments')
    honeypot = TextAreaField('',[length_honeypot])
    submit = SubmitField('Log In')