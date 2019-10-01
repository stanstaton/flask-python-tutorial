from flask import Flask, render_template, Blueprint, request

operators_blueprint = Blueprint('operators', __name__, url_prefix="/operators")

@operators_blueprint.route('/', methods=('GET', 'POST'))
def index():
    if request.method == 'GET':
        return render_template('operators.html')