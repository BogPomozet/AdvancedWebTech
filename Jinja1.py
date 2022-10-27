
#http://webtech-2223-24.napier.ac.uk:5000/hello/
from flask import Flask, render_template
app=Flask(__name__)

@app.route('/hello/')
@app.route('/hello/<name>')
def hello (name=None):
    return render_template('conditional.html', name=name)

if __name__=="__main__":
    app.run(host='0.0.0.0', debug=True)