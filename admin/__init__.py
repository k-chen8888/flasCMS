from flask import render_template, flash, redirect, session, url_for, request, g
from flask.ext.login import login_user, logout_user, current_user, login_required
from flask.views import MethodView

# Allows admin to manage things the MongoDB way
from flask.ext.mongoengine.wtf import model_form

# Import anything that needs admin to manage
from index import index, models

# Import admin tools
from flask.ext.admin import Admin

index_admin = Admin(index)
