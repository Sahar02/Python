from flask import Flask 

app = Flask(__name__)

@app.route('/')
def hello_world():
    return "hello world"

@app.route('/dojo')
def dojo():
    return "dojo"

@app.route('/say/<name>')
def say(name):
    print(name)
    return "hi " + name 

# @app.route('/repeat/<int=num>/<name>')
# def repeat(name,num):
#     return name * num

if __name__=="__main__":
    app.run(debug=True)