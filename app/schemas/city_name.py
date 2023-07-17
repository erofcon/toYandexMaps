from pydantic import BaseModel


class CityNameBase(BaseModel):
    clid: str
    description: str


class CityNameCreate(CityNameBase):
    pass


class CityNames(CityNameBase):
    id: int

    class Config:
        orm_mode = True
