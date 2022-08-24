from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'asdfghjkpoiuytrewq'
import random           # import the random module

@app.route('/')

def random_number():
    random.randint(1, 100)  # random number between 1-100
    if 'num' not in session:
        session['num'] = random.randint(1,100)
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def guess():
    session['number'] = int(request.form['guess number'])
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
 