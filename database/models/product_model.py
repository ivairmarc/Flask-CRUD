from database.database import Base
from sqlalchemy import Column, Integer, String, Numeric
    

class Products(Base):
    __tablename__ = 'products'
    id = Column(Integer, primary_key=True, autoincrement=True)
    plan_name = Column(String(100), nullable=False, unique=True)
    value = Column(Numeric(9, 2))
    upload = Column(String(50))
    download = Column(String(50))
    status = Column(Integer)

    def __repr__(self):
        return {self.plan_name}
    