from pydantic import BaseModel


class TransportBase(BaseModel):
    car_number: str
    imei: str
    device_id: int
    category: str
    route: str
    vehicle_type: str


class TransportCreate(TransportBase):
    pass


class Transport(TransportBase):
    id: int

    class Config:
        orm_mode = True
