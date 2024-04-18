from peewee import Model, DatabaseProxy



class BaseModel(Model):
    class Meta:
        database = DatabaseProxy()