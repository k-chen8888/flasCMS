from flask import Blueprint, request, redirect, render_template, url_for
from flask.views import MethodView

# Set up the blueprint
index_bp = Blueprint('index_bp', __name__, template_folder = 'templates')

# Class for the index page view
class IndexView(MethodView):
	def get(self):
		return render_template('/index.html')

# Register urls
index_bp.add_url_rule('/', view_func = IndexView.as_view('index_bp'))
