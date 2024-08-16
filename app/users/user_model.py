from app.database import Base
from sqlalchemy import Column, Integer, ForeignKey, String
from flask_login import UserMixin

class Users(UserMixin, Base):
    """ status 1 = Ativo """
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, autoincrement=True)
    email = Column(String(100), unique=True)
    name = Column(String(100), nullable=False)
    password = Column(String(100), nullable=False)
    status = Column(Integer)
    group = Column(Integer, ForeignKey('groups.id'), nullable=False)

    def __repr__(self):
        return f'<User {self.name}>'
    