from flask import Blueprint, render_template, request

loader_blueprint = Blueprint("loader_blueprint", __name__, template_folder='templates', url_prefix='/loader')


@loader_blueprint.route('/post')
def create_post():
    pass