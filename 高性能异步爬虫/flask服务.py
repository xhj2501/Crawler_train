from flask import Flask
import time

app = Flask(__name__)


@app.route('/xhj')
def index_xhj():
    time.sleep(2)
    return "Hello xhj"

@app.route('/Xhj')
def index_Xhj():
    time.sleep(2)
    return "Hello Xhj"

@app.route('/jxh')
def index_jxh():
    time.sleep(2)
    return "Hello jxh"

app.run(threaded=True)
