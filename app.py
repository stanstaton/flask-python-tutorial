# YOUR FLASK APP HERE
#Imports
from flask import Flask, render_template
from blueprints.loops import loops_blueprint
from blueprints.operators import operators_blueprint

#Instantiate App
app = Flask(__name__)

#Home Route
@app.route('/')
def Home():
    return render_template('home.html')

#blueprints
app.register_blueprint(operators_blueprint)
app.register_blueprint(loops_blueprint)


if __name__ == '__main__':
    app.run(debug=True)