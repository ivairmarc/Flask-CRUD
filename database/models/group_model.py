from database.database import Base
from sqlalchemy import Column, Integer, String


class Groups(Base):
    __tablename__ = 'groups'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False, unique=True)
    note = Column(String(100))
    status = Column(Integer)
   
    def __repr__(self):
        return self.name
    