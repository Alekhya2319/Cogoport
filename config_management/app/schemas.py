 # app/schemas.py
from pydantic import BaseModel
from typing import Optional

class CountryConfigurationBase(BaseModel):
    country_code: str

class CountryConfigurationCreate(CountryConfigurationBase):
    requirements: dict

class CountryConfigurationUpdate(BaseModel):
    requirements: dict

class CountryConfigurationInDB(CountryConfigurationBase):
    id: int
    requirements: dict

class CountryConfigurationOut(CountryConfigurationBase):
    id: int
    requirements: dict

class CountryConfigurationDeleteResponse(BaseModel):
    message: str
