# Admin requires the User definition from index
from index.util import *
index = import_index(['index', 'index_db', 'index_bcrypt'])
index_models = import_index_models(['BaseUser', 'make_user'])

class User(index_models.BaseUser):
	is_admin = index.index_db.BooleanField(default = False)
