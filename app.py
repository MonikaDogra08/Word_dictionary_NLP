import nltkmodules
from logging import debug
from flask import Flask,render_template,request
from textblob import Word

# craete a flask app
app = Flask(__name__)

# define an api
@app.route('/')
def welcome():
    return render_template('base.html') 

@app.route("/explain", methods = ["POST"])
def explain():
    # get the info:
    word = request.form.get('Word')

    # take the word to expalin and give its definition
    output = Word(word).definitions

    # check :
    if not output:
        return render_template('base.html',Explaination = f"Please enter a valid word")
    else:
        return render_template('base.html',Explaination = f"{word} means : {output}")


if __name__ == '__main__':
    
    app.run()