from flask import Flask, render_template, request, Blueprint

loops_blueprint = Blueprint('loops', __name__, url_prefix='/loops')
@loops_blueprint.route('/')
def index():
    return render_template('loops.html')