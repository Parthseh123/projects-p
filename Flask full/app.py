from pickle import TRUE
from flask import Flask,render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template('index.html')

@app.route("/products")
def products():
    return "<h1>My products</h1>"
    

if(__name__ =="__main__"):
    app.run(debug=True)