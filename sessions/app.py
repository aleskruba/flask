from flask import Flask,render_template,request,session,redirect,url_for
from datetime import timedelta

app = Flask(__name__)
app.secret_key = 'ales'
#app.permanent_session_lifetime = timedelta(days=5)

@app.route('/')
def home():
    return  render_template('home.html')

@app.route('/login',methods=['GET','POST'])
def login():
    if request.method == "POST":
      # session.permanent = True
        user = request.form['user']
        session["user"] = user
        return  redirect(url_for('user'))
    else:
        if "user" in session:
            return  redirect(url_for("user"))

        return render_template('home.html')

@app.route('/user')
def user():
    if "user" in session:
        user = session["user"]
        return  f"<h1>hello {user} </H1>"
    else:
        return redirect(url_for('home'))

@app.route('/logout')
def logout():
    session.pop("user",None)
    return redirect(url_for('home'))

if __name__== "__main__":
    app.run(port=5003)
