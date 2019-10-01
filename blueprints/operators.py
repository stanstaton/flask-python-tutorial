from flask import Flask, render_template, Blueprint, request, redirect
from models.index import db

operators_blueprint = Blueprint('operators', __name__, url_prefix="/operators")

@operators_blueprint.route('/', methods=('GET', 'POST'))
def index():
    if request.method == 'GET':
        return render_template('operators.html')
    elif request.method == 'POST':
        db.operators.insert_one({
            'name': request.form['name'],
            'uses': request.form['uses'],
            'description': request.form['description'],
            'symbol': request.form['symbol'],
            'example': request.form['example']
        })
        return redirect('/operators')