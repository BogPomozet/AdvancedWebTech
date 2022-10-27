#send a name as a URL encoded parameter 

#http://webtech-2223-24.napier.ac.uk:5000/hello/
#http://webtech-2223-24.napier.ac.uk:5000/hello/?name=valentina

from flask import Flask, request
app=Flask(__name__)

@app.rout("/hello/")
def hello():
    name= request.args.get('name','')
    if name == '':
        return "no param supplied"
    else:
        return "Hello %s " % name

if __name__=="__main__":
    app.run(host='0.0.0.0', debug=True)