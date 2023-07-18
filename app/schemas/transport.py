from pydantic import BaseModel


class TransportBase(BaseModel):
    car_number: str
    imei: str
    category: str
    vehicle_type: int
    city_name: int
    send: bool
    route: int


class TransportCreate(TransportBase):
    pass


class Transport(TransportBase):
    id: int
    device_id: int

    class Config:
        orm_mode = True


class GetTransportData(BaseModel):
    device_id: int
    category: str
    route: str
    vehicle_type: str

    class Config:
        orm_mode = True
