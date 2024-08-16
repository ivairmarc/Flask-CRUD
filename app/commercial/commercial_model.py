from app.database import Base
from sqlalchemy import Column, Integer, String


class CommercialOrigin(Base):
    __tablename__ = 'commercial_origin'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False, unique=True)
    note = Column(String(100))
    status = Column(Integer)

    def __repr__(self):
        return {self.name}
    