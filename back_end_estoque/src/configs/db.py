from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker

engine = create_engine('mysql+pymysql://root:mudar123@172.17.0.2:3306/estoque')

Session = sessionmaker(bind=engine)
session = Session()
