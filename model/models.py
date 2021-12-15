import datetime
from sqlalchemy import Column, Integer, String, Date, Sequence, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.sql.sqltypes import DECIMAL, INT, VARCHAR, DateTime, Time

Base = declarative_base()



class Usuario(Base):
    __tablename__ = 'usuario'
    id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
    email = Column(String(255), unique=True, nullable=False)
    senha = Column(String(45), nullable=False)
    def __repr__(self):
        return f'Usuario {self.nome}'
    @classmethod
    def find_by_email(cls, session, email):
        return session.query(cls).filter_by(email=email).one()

class Atividade(Base):
    __tablename__ = 'atividade'
    id = Column(Integer, Sequence('publica_id_seq'), primary_key=True)
    id_usuario = Column(Integer, ForeignKey('usuario.id'))
    inicio = Column(Date, unique=False, nullable=False)
    fim = Column(Date, unique=False, nullable=False)
    quilometros = Column(DECIMAL(10,2),unique=False, nullable=False)
    tipo_atividade = Column(VARCHAR(45), unique=False, nullable=False)
    local = Column(VARCHAR(255), unique=False, nullable=False)

class Curtida(Base):
    __tablename__ = 'curtida'
    id_curtida =  Column(Integer, Sequence('publica_id_seq'), primary_key=True)
    id_atividade = Column(Integer, ForeignKey('atividade.id'))
    usuario_id = Column(Integer, ForeignKey('usuario.id'))
    usuario = relationship("Usuario", backref="Curtida")
    atividade = relationship("Atividade", backref="Curtida")

class Comentario(Base):
    __tablename__ = 'comentario'
    id = Column(Integer, Sequence('publica_id_seq'), primary_key=True)
    id_usuario = Column(Integer, ForeignKey('usuario.id'))
    id_atividade = Column(Integer, ForeignKey('atividade.id'))
    comentario = Column(VARCHAR(255), unique=True, nullable=False)
    usuario = relationship("Usuario", backref="Comentario")
    atividade = relationship("Atividade", backref="Comentario")
