from playhouse.flask_utils import FlaskDB


db = FlaskDB()

class BaseModel(db.Model):
    pass