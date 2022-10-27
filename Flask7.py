#URL Variable that enables to retieve a user's details by name
#http://webtech-2223-24.napier.ac.uk:5000/hello/?name=valentina

from flask import Flask
app = Flask(__name__)

@app.route("/hello/<name>")
def hello(name):
    return "Hello %s" % name

#http://webtech-2223-24.napier.ac.uk:5000/add/10/20
@app.route("/add/<int:first>/<int:second>")
def add(first, second):
    return str(first+second)

if __name__=="__main__":
    app.run(host='0.0.0.0', debug=True)