from factory import DatabaseFactory


factory = DatabaseFactory()
database = factory.process("Sqlite")
print(database.get_db_uri())