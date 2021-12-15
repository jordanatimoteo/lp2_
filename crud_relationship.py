from sqlalchemy import create_engine, or_
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql.expression import desc


from model.models import Comentario, Curtida, Usuario, Atividade

engine = create_engine(
    "mysql+pymysql://root:@localhost/python", echo=True)

Session = sessionmaker(bind=engine)
session = Session()

def delete(valor):
    atividade = session.query(Atividade).order_by(desc(Atividade.local))
    for atividade in atividade:
        if(atividade.local == valor):
          session.delete(atividade)
          session.commit()
def update_senha(achado,valor):
    user = Usuario.find_by_email(session=session, email=achado)
    user.senha = valor
    session.commit()
def select_VGA():
    tuplas = session.query(Atividade).order_by(desc(Atividade.quilometros))
    for tupla in tuplas:
        if(tupla.local == "VGA"):
            print(tupla.id_usuario," - ", tupla.quilometros , " - ", tupla.inicio, " - ", tupla.fim)
def create1():
    user1 = Usuario(email='usu1@usu.com', senha='123')
    session.add(user1)
    session.commit()
    atividade1 = Atividade(id="1",id_usuario="1",inicio='2021-11-17',fim='2021-12-11',quilometros='20',tipo_atividade='Xadrez', local='TC')
    session.add(atividade1)
    atividade2 = Atividade(id="2",id_usuario="1",inicio='2021-11-16',fim='2021-12-12',quilometros='30',tipo_atividade='Corrida Maluca', local='VGA')
    session.add(atividade2)
    atividade3 = Atividade(id="3",id_usuario="1",inicio='2021-11-15',fim='2021-12-13',quilometros='20',tipo_atividade='Judo', local='VGA')
    session.add(atividade3)
    session.commit()
def create2():
    user2 = Usuario(email='usu2@usu.com', senha='1233543')
    session.add(user2)
    session.commit()
    atividade1 = Atividade(id="4",id_usuario="2",inicio='2021-11-18',fim='2021-12-15',quilometros='40',tipo_atividade='Ciclismo', local='VGA')
    session.add(atividade1)
    atividade2 = Atividade(id="5",id_usuario="2",inicio='2021-11-18',fim='2021-12-15',quilometros='50',tipo_atividade='Corrida', local='VGA')
    session.add(atividade2)
    atividade3 = Atividade(id="6",id_usuario="2",inicio='2021-11-18',fim='2021-12-15',quilometros='60',tipo_atividade='skateboarding', local='TC')
    session.add(atividade3)
    session.commit()
def create3():
    user3 = Usuario(email='usu3@usu.com', senha='12345678')
    session.add(user3)
    session.commit()
    atividade1 = Atividade(id="7",id_usuario="3",inicio='2021-11-18',fim='2021-12-15',quilometros='0',tipo_atividade='LOL', local='VGA')
    session.add(atividade1)
    atividade2 = Atividade(id="8",id_usuario="3",inicio='2021-11-18',fim='2021-12-15',quilometros='10',tipo_atividade='Corrida', local='VGA')
    session.add(atividade2)
    atividade3 = Atividade(id="9",id_usuario="3",inicio='2021-11-18',fim='2021-12-15',quilometros='10',tipo_atividade='Patins', local='TC')
    session.add(atividade3)
    session.commit()
def curtir():
    curtida1 = Curtida(id_atividade='3', usuario_id='1')
    session.add(curtida1)
    session.commit()
    curtida2 = Curtida(id_atividade='2',usuario_id='2')
    session.add(curtida2)
    session.commit()
def comentar():
    comentario1 = Comentario(id="1",id_usuario='1',id_atividade='3',comentario='Legal')
    session.add(comentario1)
    session.commit()
    comentario2 = Comentario(id="2",id_usuario='3',id_atividade='2',comentario='muito legal')
    session.add(comentario2)
    session.commit()
    comentario3 = Comentario(id="3",id_usuario='2',id_atividade='1',comentario='Dahoras')
    session.add(comentario3)
    session.commit() 
    comentario4 = Comentario(id="4",id_usuario='3',id_atividade='1',comentario='Massa')
    session.add(comentario4)
    session.commit() 


create1()
create2()
create3()
curtir()
comentar()
select_VGA()
update_senha('usu1@usu.com','senhausu1')
delete('VGA')