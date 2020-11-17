from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/')
def index():
    name='pepa'
    return render_template('Index.html',name=name)

@app.route('/classmates')
def classmates():
    listname=['Jan','Jiri']
    return render_template('classmates.html',listname=listname)


if __name__=='__main__':
    app.run(port=8000)
