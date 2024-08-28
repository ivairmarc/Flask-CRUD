from app.database import Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship


# Modelagem da tabela Groups
class Groups(Base):
    __tablename__ = 'groups'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False, unique=True)
    note = Column(String(100))
    status = Column(Integer)
   
    # Relacionamento bidirecional com a tabela Users
    users = relationship('Users', secondary='user_groups', back_populates='groups')

    def __repr__(self):
        return f'<Group {self.name}>'

    
class Permissions(Base):
    __tablename__ = 'permissions'
    id = Column(Integer, primary_key=True, autoincrement=True)
    module = Column(String(30), nullable=False)
    permission = Column(String(100), nullable=False, unique=True)
    name = Column(String(100), nullable=False)

    def __repr__(self):
        return f"<Permission(module='{self.module}', permission='{self.permission}', name='{self.name}')>"
        

class PermissionsGroup(Base):
    __tablename__ = 'permissions_group'
    id = Column(Integer, primary_key=True, autoincrement=True)
    group_id = Column(Integer, ForeignKey('groups.id'), nullable=False)
    permission_id = Column(Integer, ForeignKey('permissions.id'), nullable=False, unique=True)
    habilite = Column(String(1), default='N', nullable=False)
    allow_custody = Column(String(1), default='N', nullable=False)
    note = Column(String(100))

    permission_obj = relationship('Permissions', backref='permissions_groups', foreign_keys=[permission_id])

    def __repr__(self):
        return f"habilite='{self.habilite}', allow_custody='{self.allow_custody}')>"
    