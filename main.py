from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def welcome():
    return '''
    <html>
    
        <head><title>Welcome</title></head>
        <body>
            <h1>Welcome to Flask framework!</h1>
            <p>This should be amazing!</p>  
        </body>
    </html>
    '''

@app.route("/index", methods=['GET'])
def index():
    return render_template('index.html')

@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/form", methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        return f"Received name: {name} <br> email: {email}"

    return render_template('form.html')

@app.route('/example', methods=['GET'])
def example():
    return render_template('example.html')


if __name__ == '__main__':
    app.run(debug=True)