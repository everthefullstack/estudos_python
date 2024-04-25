from factory import DatabaseFactory


factory = DatabaseFactory()
database = factory.process("mysql")
print(database.get_db_uri())

