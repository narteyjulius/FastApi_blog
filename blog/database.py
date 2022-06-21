from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from blog.config import settings


# settings = config.settings

# SQLALCHEMY_DATABASE_URL = 'postgresql://<username>:<password>@<ip-address/hostname>/<database_name>'
print("Connecting to database")


SQLALCHEMY_DATABASE_URL = f'postgresql://{settings.database_username}:{settings.database_password}@{settings.database_hostname}:{settings.database_port}/{settings.database_name}'

engine = create_engine(SQLALCHEMY_DATABASE_URL)

#to communicate with the sql database.
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# Dependency
#sessionLocal will take to the database.(connect to database)
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

#We dont need this because we are using sqleachemy but still can be used
# while True:
        
#     try:
#         conn = psycopg2.connect(host='localhost', database='fastapi', user='postgres', password='postgres', cursor_factory=RealDictCursor)
#         cursor = conn.cursor()
#         print("Database connection was succesful")
#         break

#     except Exception as error:
#         print("Connection to database failed")
#         print("Error Type: ", error)
#         time.sleep(3)