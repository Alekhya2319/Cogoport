# app/api/endpoints.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..database import SessionLocal, engine
from ..crud import get_configuration, create_configuration, update_configuration, delete_configuration
from ..schemas import ConfigurationCreate, ConfigurationUpdate, ConfigurationOut, ConfigurationDeleteResponse

router = APIRouter()

# Dependency to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/create_configuration", response_model=ConfigurationOut)
def create_config(config_data: ConfigurationCreate, db: Session = Depends(get_db)):
    db_config = create_configuration(db, country_code=config_data.country_code, requirements=config_data.requirements)
    return db_config

@router.get("/get_configuration/{country_code}", response_model=ConfigurationOut)
def get_config(country_code: str, db: Session = Depends(get_db)):
    db_config = get_configuration(db, country_code)
    if db_config is None:
        raise HTTPException(status_code=404, detail="Configuration not found")
    return db_config

@router.put("/update_configuration/{country_code}", response_model=ConfigurationOut)
def update_config(country_code: str, config_data: ConfigurationUpdate, db: Session = Depends(get_db)):
    updated_config = update_configuration(db, country_code, config_data.requirements)
    if updated_config is None:
        raise HTTPException(status_code=404, detail="Configuration not found")
    return updated_config

@router.delete("/delete_configuration/{country_code}", response_model=ConfigurationDeleteResponse)
def delete_config(country_code: str, db: Session = Depends(get_db)):
    deleted_config = delete_configuration(db, country_code)
    if deleted_config is None:
        raise HTTPException(status_code=404, detail="Configuration not found")
    return {"message": f"Deleted configuration with country code: {country_code}"}
