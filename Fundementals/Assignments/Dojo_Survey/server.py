from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'qwertyuiopljhgdsa'


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def index():
    return redirect('/result')

@app.route('/result')
def index():
    
    return render_template('results.html')

# @app.route('/result')
# def index():
#     return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
 