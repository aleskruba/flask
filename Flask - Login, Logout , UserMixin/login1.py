from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager,logout_user,login_required,login_user,current_user,UserMixin

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database1.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)

class User(UserMixin,db.Model):
    id  = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(20),unique=True)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route('/')
def index():
    user = User.query.filter_by(username='ales').first()
    login_user(user)
    return  "You are now logged in"

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return "you are now logged out"

@app.route('/home')
@login_required
def home():
    return "the current user is " + current_user.username

if __name__== "__main__":
    app.run(port=5003)