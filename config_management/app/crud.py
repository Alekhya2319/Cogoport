 # app/crud.py
from sqlalchemy.orm import Session
from .models import CountryConfiguration

def get_configuration(db_session: Session, country_code: str):
    return db_session.query(CountryConfiguration).filter(CountryConfiguration.country_code == country_code).first()

def create_configuration(db_session: Session, country_code: str, requirements: dict):
    db_config = CountryConfiguration(country_code=country_code, requirements=requirements)
    db_session.add(db_config)
    db_session.commit()
    db_session.refresh(db_config)
    return db_config

def update_configuration(db_session: Session, country_code: str, new_requirements: dict):
    config = db_session.query(CountryConfiguration).filter(CountryConfiguration.country_code == country_code).first()
    if config:
        config.requirements = new_requirements
        db_session.commit()
        db_session.refresh(config)
    return config

def delete_configuration(db_session: Session, country_code: str):
    config = db_session.query(CountryConfiguration).filter(CountryConfiguration.country_code == country_code).first()
    if config:
        db_session.delete(config)
        db_session.commit()
    return config