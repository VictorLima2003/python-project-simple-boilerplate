from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# O que é uma session?

class DBConnectionHandler:
    
    def __init__(self):
        # __ esses dois anderlines segnificam que esse é um atributo privado.
        self.__connection_string = "{}://{}:{}@{}:{}/{}".format(
            "mysql+pymysql",
            'root',
            'victor',
            'localhost',
            '3306',
            'clean_database'
        )

        self.__engine = self.__create_database_engine()
        self.session = None

    def __create_database_engine(self):
        engine = create_engine(self.__connection_string)
        return engine

    def get_engine(self):
        return self.__engine
    
    def __enter__(self):
        session_make = sessionmaker(bind=self.__engine)
        self.session = session_make()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.session.close()