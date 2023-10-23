from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class ElementsToProcess(Base):
    __tablename__ = 'ElementsToProcess'
    id = Column(Integer, primary_key=True)
    idBulk = Column(Integer, nullable=False)
    retries = Column(Integer)
    status = Column(Integer, nullable=False)
    name = Column(String(100), nullable=False)

    def __str__(self):
        return {
            'id': self.id,
            'idBulk': self.idBulk,
            'retries': self.retries,
            'status': self.status,
            'name': self.name,
        }
