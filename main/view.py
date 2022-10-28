from flask import Blueprint, render_template, request

main_blueprint = Blueprint("main_blueprint", __name__, template_folder='templates', url_prefix='/')


@main_blueprint.route('/')
def main_page():
    return render_template('index.html')


@main_blueprint.route('/search')
def main_page():
    substr = request.args.get('s')

    return render_template('index.html')