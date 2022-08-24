from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = "good morning sunshine hahahahaha"

@app.route('/')
def index():
    if 'views' not in session:
        session ['views'] = 0
    session['views'] += 1

    if 'views' in session:
        print('key exists!')
    else:
        print("key 'views' does NOT exist")
    return render_template('index.html')

@app.route('/destroy_session')
def counter():
    session.clear()		# clears a specific key
    return redirect('/')

@app.route('/count_plus2')
def countplustwo():
    if 'views' not in session:
        session ['views'] = 0
    session['views'] += 2
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)