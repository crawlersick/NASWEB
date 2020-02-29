from flask import Flask,render_template,url_for
from flask import jsonify
import myutils.getDindex
import os
import urllib
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

auth = HTTPBasicAuth()

users = {
    "john": generate_password_hash("123")
}

@auth.verify_password
def verify_password(username, password):
    if username in users:
        return check_password_hash(users.get(username), password)
    return False

@app.route('/')
@auth.login_required
def hello_world():
    #return 'Hello, World!'
    return render_template('home.html')

@app.route('/toplist')
def toplist():
    a=myutils.getDindex.SysSetting()
    a.updateattr()
    return jsonify(a.itemlist0)

@app.route('/l2/<epname>')
def l2list(epname):
    a=myutils.getDindex.SysSetting()
    a.updatedatamap(epname)
    return jsonify(a.datamap[epname])

@app.route('/l3/<foldername>/<epname>')
def l3list(foldername,epname):
    epname=epname.replace('-->',os.sep)

    filename=os.path.join("/static/Downloads/",foldername,epname)
    filename=urllib.parse.quote(filename)
    return render_template('play.html',filename=filename,subname=filename+".vtt")


if __name__ == '__main__':
    print("start...")
    app.run(host='0.0.0.0')
