from typing import Union
from playhouse.flask_utils import FlaskDB
from flask_sqlalchemy import SQLAlchemy


db: Union[FlaskDB, SQLAlchemy] = None