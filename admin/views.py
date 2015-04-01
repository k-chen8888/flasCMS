from flask import Blueprint, request, redirect, render_template, url_for
from flask.views import MethodView

# Set up the blueprint
admin_bp = Blueprint('admin_bp', __name__, template_folder = 'templates')

# Class for the admin page view
class AdminView(MethodView):
	def get(self):
		return render_template('/admin.html')

# Register urls
admin_bp.add_url_rule('/admin', view_func = AdminView.as_view('admin_bp'))
