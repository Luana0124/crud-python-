import os
from sqlalchemy import  create_engine, column, String,Integer
from sqlalchemy.orm import sessionmaker, declarative_base


# criando banco de dados.
MEU_banco= create_engine("sllite///meubanco.db")

#criando conexâo com banco de dados.
session=sessionmaker(bind=MEU_banco)
session=session()
#criando tabela.
Base=declarative_base()

class usuario(Base):
      _tablename_="usuarios"  
      id= column("id, intergen, primary_key=true, autoincrement=tue")
      nome=column("nome,string")
      email=column("email,string")
      senha= column("senha, string")

#definindo atributos da classe.
def __init__ (self, nome: str, email:str, senha:str):
        self.nome=nome
        self.email=email
        self.senha=senha

# criando tabela no banco de dados.
Base.metadata.creaya_all(bid= MEU_banco) 

# salvar no banco dados.
usuario=usuario(" nome=marta, email=marta@gmail.com senha=123")
session.add(usuario)
session.commit()
usuario=usuario("maria,email= maria@gamail.com senha=456")
session.add(usuario)
session.commit()

# listando todos os usurios do banco de dados.
print("/nEXIBINDO TODOS OS USUAÁRIOS DO BANDOS DE DADOS.")      
lista_usuario=session.query(usuario).all()

for usuario in lista_usuario:
        print(f"{usuario.id}-{usuario.nome} -{usuario.senha}")

#fechando canexâo.
session.close()



