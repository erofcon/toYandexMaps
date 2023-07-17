from sqlalchemy import MetaData, Table, Column, Integer, ForeignKey, String, Enum

from .route import route
from .vehicle_type import vehicle_type

metadata = MetaData()


class CategoryType(str, Enum):
    slow = 's'
    ordinary = 'n'


transport = Table(
    'transport', metadata,
    Column('id', Integer(), primary_key=True),
    Column('car_number', String()),
    Column('imei', String()),
    Column('device_id', Integer()),
    Column('category', CategoryType(), default=CategoryType.slow),
    Column('route', String(), ForeignKey(route.c.route)),
    Column('vehicle_type', String(), ForeignKey(vehicle_type.c.vehicle_type)),
)
