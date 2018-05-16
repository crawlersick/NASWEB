from flask import Flask,render_template,url_for
from flask import jsonify
import myutils.getDindex
import os
import urllib

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

@app.route('/')
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
    return render_template('play.html',filename=filename)


if __name__ == '__main__':
    print("start...")
    app.run(host='0.0.0.0')
