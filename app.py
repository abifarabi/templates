from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def welcome():
    return 'Welcome to Flask framework! This should be amazing!'

@app.route('/index')
def index():
    return 'Welcome to the index page!'

@app.route('/arkan')
def arkan():
    return '''
            <h1>SAYA ARKAN, KAMU SIAPA?</h1>
'''

@app.route('/inspirasi')
def inspirasi():
    return render_template('inspriasi.html')

if __name__ == '__main__':
    app.run(debug=True)