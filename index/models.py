from index import db

class Users(db.Document):
	username = db.StringField(max_length = 32, required = True)

	meta = {
		'allow_inheritance' = True
	}
