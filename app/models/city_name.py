from sqlalchemy import MetaData, Table, Column, Integer, String

metadata = MetaData()

city_name = Table(
    'city_name', metadata,
    Column('id', Integer(), primary_key=True),
    Column('clid', String()),
    Column('description', String()),
)