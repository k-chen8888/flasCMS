from index import index_db as db, index_bcrypt as bc

class BaseUser(db.Document):
	username = db.StringField(max_length = 32, required = True, unique = True)
	pw_hash = db.StringField(max_length = 60, required = True)
	
	meta = {
		'allow_inheritance': True
	}

# Makes a User object to insert into the database
def make_user(user, pw):
	return BaseUser( username = user, pw_hash = bc.generate_password_hash(pw) )
