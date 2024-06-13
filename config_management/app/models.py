 # app/models.py

from sqlalchemy import Column, Integer, String, JSON

from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class CountryConfiguration(Base):
    __tablename__ = 'country_configurations'

    id = Column(Integer, primary_key=True, index=True)
    country_code = Column(String, unique=True, index=True)
    business_name = Column(String)
    registration_number = Column(String)
    additional_details = Column(JSON)
 