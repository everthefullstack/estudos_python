from app.models.peewee.usuario_model import UsuarioModel


class Tables:
    
    def __create_tables(self):
        
        tables = [UsuarioModel,]
        
        for table in tables:
            try:
                if table.table_exists():
                    print(f"Tabela {table._meta.table_name} já existe, não será criada.")
                    
                else:
                    table.create_table(safe=True)
                    print(f"Tabela {table._meta.table_name} criada com sucesso!")

            except Exception as error:
                print(f"Erro ao criar tabela => {error}")
                
    def process(self):
        self.__create_tables()

def process():
    Tables().process()
