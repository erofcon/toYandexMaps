from pydantic import BaseModel


class CityNameBase(BaseModel):
    clid: str
    description: str
    send: bool


class CityNameCreate(CityNameBase):
    pass


class CityNames(CityNameBase):
    id: int

    class Config:
        orm_mode = True
