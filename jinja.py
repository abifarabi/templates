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

# variable rule
# @app.route("/success/<int:score>")
# def success(score):
#     return "The marks you got is " + str(score)

# Dynamic variable in URL
@app.route("/success/<int:score>")
def success(score):
    result = ''
    if score >= 75:
        result = "Congratulations! You passed the exam!"
    else:
        result = "Sorry, you did not pass the exam."

    return render_template('result.html', results=result)

# Jinja2 Template Engine
'''
{{ variable }} - for displaying/printing variables in html
{% ... %} - for conditional statements, loops, etc
{# ... #} - for comments in Jinja2 Templates
'''

@app.route("/jinja_exa/<int:score>")
def jinja_exa(score):
    result = ''
    if score >= 75:
        result = "Congratulations! You passed the exam!"
    else:
        result = "Sorry, you did not pass the exam."

    return render_template('jinja_exa.html', results=result)


if __name__ == '__main__':
    app.run(debug=True)