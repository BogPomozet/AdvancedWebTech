from flask import Flask, session

app=Flask(__name__)
app.secret_key='A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'

@app.route('/')
def index():
    return "Root route for the session example"

@app.route('session/write/<name>/')
def write(name=None):
    #Set key=value, name=simon into session
    session['name']=name
    return "Wrote %s into 'name' key of session" % name

@app.route('session/read/')
def read():
    try:
        if(session['name']):
            return str(session['name'])
    except KeyError:
        pass
    return "No session variable set for 'name' key"

@app.route('session/remove/')
def remove():
    session.pop('name', None)
    return "Removed key 'name' form session"

if __name__=="__main__":
    app.run(host='0.0.0.0', debug=True)

