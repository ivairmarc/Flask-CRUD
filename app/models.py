from app.database import Base
from sqlalchemy import Column, Integer, ForeignKey, String, Numeric


class Groups(Base):
    __tablename__ = 'groups'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False, unique=True)
    note = Column(String(100))
    status = Column(Integer())
   
    def __repr__(self):
        return self.name
    

class Users(Base):
    """ status 1 = Ativo """
    __tablename__ = 'users'
    id = Column(Integer, autoincrement=True)
    email = Column(String(100), primary_key=True, unique=True)
    name = Column(String(100), nullable=False)
    password = Column(String(100), nullable=False)
    status = Column(Integer())
    group = Column(Integer(), ForeignKey('groups.id'))


    def __repr__(self):
        return f'<User {self.name}>'
    

class Products(Base):
    __tablename__ = 'products'
    id = Column(Integer, primary_key=True, autoincrement=True)
    plan_name = Column(String(100), nullable=False, unique=True)
    value = Column(Numeric(9, 2))
    upload = Column(String(50))
    download = Column(String(50))
    status = Column(Integer())

    def __repr__(self):
        return {self.plan_name}
    

class CommercialOrigin(Base):
    __tablename__ = 'commercial_origin'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False, unique=True)
    note = Column(String(100))
    status = Column(Integer())

    def __repr__(self):
        return {self.name}


class Leads(Base):
    __tablename__ = 'leads'
    id = Column(Integer, primary_key=True, autoincrement=True)
    cpf = Column(String(100), nullable=False, unique=True)
    adress = Column(String(100), nullable=False)
    number = Column(String(100))
    neighborhood = Column(String(100))
    city = Column(String(100))
    state = Column(String(100))
    product = Column(String(50), ForeignKey('products.id'))
    commercial_origin = Column(String(50), ForeignKey('commercial_origin.id'))
    create_at = Column(String(100), ForeignKey('users.email'))
    altered_at = Column(String(100), ForeignKey('users.email'))

    def __repr__(self):
        return {self.cpf}
