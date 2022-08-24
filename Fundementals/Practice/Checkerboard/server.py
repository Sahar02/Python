from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def checkerboard():
    return render_template('index.html')

@app.route('/4')
def four_colums():
    return render_template('RowandColums.html',num=8)


if __name__=="__main__":
    app.run(debug=True)