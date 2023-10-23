from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

db_credentials = {
    'username': 'masleads',
    'password': 'masleads-pwd',
    'host': 'localhost',
    'db_name': 'masleads',
}
db_url = "postgresql://{username}:{password}@{host}/{db_name}".format(**db_credentials)

engine = create_engine(db_url)

Session = sessionmaker(bind=engine)
