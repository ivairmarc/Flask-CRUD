from app.database import Base
from sqlalchemy import Column, Integer, String
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
    