import pandas as pd

from sqlalchemy import  create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import json
from sqlalchemy import insert, select

# from .config import DB_HOST, DB_NAME, DB_PASS, DB_PORT, DB_USER

DATABASE_URL = f"postgresql://{'postgres'}:{'0013jqfqA'}@{'localhost'}:{5432}/{'WEB'}"
Base = declarative_base()


engine = create_engine(DATABASE_URL)
# async_session_maker = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)
session = sessionmaker(bind=engine)
s = session()

from sqlalchemy import DateTime, MetaData, Table, Column, Integer, String, JSON
import datetime

metadata = MetaData()



raw_data = Table(
    'raw_data',
    metadata,
    Column('id_data', Integer, primary_key=True),
    Column('country', String),
    Column('category', String),
    Column('name', String),
    Column('brand', String),
    Column('price', String),
    Column('created_at', DateTime, default=datetime.datetime.now),
    Column('update_at', DateTime, default=datetime.datetime.now),
    Column('specifications', JSON),
    Column('url', String),
    Column('img_href', String),
    Column('net_href', String),
)

log_changes = Table(
    'log_changes',
    metadata,
    Column('id_changes', Integer, primary_key=True),
    Column('dite_changes',DateTime, default=datetime.datetime.now),
    Column('log_change',String)
)



# async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
#     async with async_session_maker() as session:
#         yield session

# def select_data(s):
#        result = s.execute(select(raw_data))
#        for i in result:
#            print(i)
#        return result

def create_xlsx_file():

    total_row_data = pd.read_sql("select * from \"raw_data\"", engine)
    changes_log_data = pd.read_sql("select * from \"log_changes\"", engine)

    with pd.ExcelWriter('test.xlsx') as writer:
        total_row_data.to_excel(writer, sheet_name='All Data', index=False)
        changes_log_data.to_excel(writer, sheet_name='Changes', index=False)


create_xlsx_file()