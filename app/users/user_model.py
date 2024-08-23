from sqlalchemy import Column, Integer, ForeignKey, String, Date
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
    position = Column(String(100), nullable=False)
    passwd_expires = Column(String(1), default='N')
    passwd_change_befor = Column(String(1), default='N')
    password = Column(String(500), nullable=False)
    status = Column(Integer)
    create_at = Column(Date())
    
    # Relacionamento bidirecional com a tabela Groups
    groups = relationship('Groups', secondary='user_groups', back_populates='users')

    def __repr__(self):
        return f'<User {self.name}>'
