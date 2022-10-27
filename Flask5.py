#Implementing some other error codes

from flask import Flask, abort
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World'

@app.route('/force404')
def force404():
    abort(404)

@app.erorrorhandler(404)
def page_nor_found(error):
    return "Couldn't find the page you requested", 404

if __name__=="__main__":
    app.run(host='0.0.0.0', debug=True)