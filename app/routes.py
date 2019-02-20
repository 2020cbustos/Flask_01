from flask import *
from app import app
from app.models import giphy

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/form')
def form():
    return render_template('form.html')


@app.route('/shodata',methods=['GET','POST'])
def shodata():
    userdata= dict(request.form)
    print(userdata)
    return render_template('shodata.html', name=userdata['name'][0], age=userdata['age'][0])

@app.route('/api_request',methods=['GET','POST'])
def api_request():
    return render_template('api_request.html')


@app.route('/api_data',methods=['GET','POST'])
def api_data():
    api_data= dict(request.form)
    meme = api_data["meme"][0]
    data = giphy.api_call(meme)
    return render_template('api_data.html',data=data)
