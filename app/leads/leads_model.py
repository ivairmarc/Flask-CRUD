from app.database import Base
from sqlalchemy import Column, Integer, ForeignKey, String


class Leads(Base):
    __tablename__ = 'leads'
    id = Column(Integer, primary_key=True, autoincrement=True)
    cpf = Column(String(100), nullable=False, unique=True)
    adress = Column(String(100), nullable=False)
    number = Column(String(100))
    neighborhood = Column(String(100))
    city = Column(String(100))
    state = Column(String(100))
    product_lead = Column(Integer, ForeignKey('products.id'))
    commercial_origin = Column(Integer, ForeignKey('commercial_origin.id'))
    create_at = Column(String(100), ForeignKey('users.email'))
    altered_at = Column(String(100), ForeignKey('users.email'))

    def __repr__(self):
        return {self.cpf}
