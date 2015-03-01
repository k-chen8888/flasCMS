from flask import Flask
from flask.ext.mongoengine import MongoEngine

# Index page
index = Flask(__name__)

# Add mongoDB stuff
index.config['MONGODB_SETTINGS'] = {'DB': 'index'}
index.config['SECRET_KEY'] = 'root'

index_db = MongoEngine(index)

# Use the blueprints
def register_blueprints(index):
	# Put the blueprint import here to prevent circular imports
	from index.views import index_bp

	index.register_blueprint(index_bp)

# Call the newly defined function to actually use the blueprints
register_blueprints(index)

if __name__ == '__main__':
	index.run()
