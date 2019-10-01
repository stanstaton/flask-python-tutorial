# YOUR FLASK APP HERE
#Imports
from flask import Flask

#Instantiate App
app = Flask(__name__)

#Home Route
@app.route('/')
def Home():
    return 'MAIN PAGE STUB'


if __name__ == '__main__':
    app.run(debug=True)