import databases

# SQLALCHEMY_DATABASE_URL = f'postgres://{DB_USER}:{DB_PASS}@{DB_HOST}:5432/{DB_NAME}'

SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"
# SQLALCHEMY_DATABASE_URL = "postgresql://user:password@postgresserver/db"

database = databases.Database(url=SQLALCHEMY_DATABASE_URL)
