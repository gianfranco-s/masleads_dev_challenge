from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from os import getenv

IS_DEV = getenv('IS_DEV', 'false').lower() in ('1', 'true')

if IS_DEV:
    from dotenv import load_dotenv
    load_dotenv('../docker.env')
    host = 'localhost'
else:
    # Environment variables are loaded by docker-compose.yml
    host = 'database'  # Name of the db service defined in docker-compose.yml


db_credentials = {
    'username': getenv('POSTGRES_USR'),
    'password': getenv('POSTGRES_PWD'),
    'db_name': getenv('POSTGRES_DB'),
    'host': host,
}
db_url = "postgresql://{username}:{password}@{host}/{db_name}".format(**db_credentials)

engine = create_engine(db_url)

Session = sessionmaker(bind=engine)
