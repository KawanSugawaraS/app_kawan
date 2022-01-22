from flask import Flask, render_template

app = Flask(__name__)

# Creating simple Routes 
@app.route('/test')
def test():
    return "Home Page"

@app.route('/test/about/')
def about_test():
    return "About Page"

@app.route('/test/contact')
def contact_test():
    return "Contact Page"

@app.route('/test/tictactou')
def tictactou_test():
    return "Tictactou Page"

@app.route('/test/Memoria')
def memoria_test():
    return "Memoria Page"

@app.route('/test/Ahorcado')
def ahorcado_test():
    return "Ahorcado Page"


# Routes to Render Something
@app.route('/')
def home():
    return render_template("home.html")

@app.route('/about', strict_slashes=False)
def about():
    return render_template("about.html")

@app.route('/contact', strict_slashes=False)
def contact():
    return render_template("contact.html")

@app.route('/tictactou', strict_slashes=False)
def tictactou():
    return render_template("tictactou.html")

@app.route('/memoria', strict_slashes=False)
def memoria():
    return render_template("pares.html")

@app.route('/ahorcado', strict_slashes=False)
def ahorcado():
    return render_template("ahorcado.html")

# Make sure this we are executing this file
if __name__ == '__main__':
    app.run(debug=True)
