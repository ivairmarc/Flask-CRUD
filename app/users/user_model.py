from sqlalchemy import Column, Integer, ForeignKey, String
from sqlalchemy.orm import relationship
from flask_login import UserMixin
from app.database import Base


# Tabela associativa para o relacionamento muitos-para-muitos
class UserGroups(Base):
    __tablename__ = 'user_groups'
    id_user = Column(Integer, ForeignKey('users.id'), primary_key=True)
    id_group = Column(Integer, ForeignKey('groups.id'), primary_key=True)
    
    
# Modelagem da tabela Users
class Users(UserMixin, Base):
    """ status 1 = Ativo """
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, autoincrement=True)
    email = Column(String(100), unique=True, nullable=False)
    name = Column(String(100), nullable=False)
    password = Column(String(100), nullable=False)
    status = Column(Integer)
    
    # Relacionamento bidirecional com a tabela Groups
    groups = relationship('Groups', secondary='user_groups', back_populates='users')

    def __repr__(self):
        return f'<User {self.name}>'
