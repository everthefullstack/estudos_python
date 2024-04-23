from app.models.sqlalchemy.base_model import BaseModel
from sqlalchemy import Column, Integer, String


class UsuarioModel(BaseModel):
    __table_name__ = "tbusuario"

    id = Column(Integer, primary_key=True)
    nome = Column(String, nullable=False)
    senha = Column(String, nullable=False)
    