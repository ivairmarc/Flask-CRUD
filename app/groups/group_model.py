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
    

class PermissionsGroup(Base):
    __tablename__='permissions_group'
    id = Column(Integer, primary_key=True, autoincrement=True)
    id_group = Column(Integer, ForeignKey('groups.id'), nullable=False)
    modulo_per = Column(String(30))
    permission = Column(String(100), nullable=False, unique=True)
    name_per = Column(String(100))
    habilite_per = Column(String(1), default='N')
    allowcustody_per = Column(String(1), default='N')
    note = Column(String(100))

    def __repr__(self):
        return f'<Permission {self.name_per}>'
