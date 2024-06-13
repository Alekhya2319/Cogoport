# app/main.py

from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from app import crud, models, schemas  # Adjust this line according to your project structure

# Initialize FastAPI app
app = FastAPI()

# Dependency to get DB session
def get_db():
    db = models.SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Example route to create a country configuration
@app.post("/create_configuration", response_model=schemas.CountryConfigurationOut)
def create_configuration(config_data: schemas.CountryConfigurationCreate, db: Session = Depends(get_db)):
    return crud.create_country_config(db, config_data)

# Example route to get configuration by country code
@app.get("/get_configuration/{country_code}", response_model=schemas.CountryConfigurationOut)
def read_configuration(country_code: str, db: Session = Depends(get_db)):
    db_config = crud.get_country_config(db, country_code)
    if db_config is None:
        raise HTTPException(status_code=404, detail="Country configuration not found")
    return db_config

# Example route to update configuration by country code
@app.put("/update_configuration/{country_code}", response_model=schemas.CountryConfigurationOut)
def update_configuration(country_code: str, config_data: schemas.CountryConfigurationCreate, db: Session = Depends(get_db)):
    db_config = crud.update_country_config(db, country_code, config_data)
    if db_config is None:
        raise HTTPException(status_code=404, detail="Country configuration not found")
    return db_config

# Example route to delete configuration by country code
@app.delete("/delete_configuration/{country_code}", response_model=schemas.CountryConfigurationOut)
def delete_configuration(country_code: str, db: Session = Depends(get_db)):
    db_config = crud.delete_country_config(db, country_code)
    if db_config is None:
        raise HTTPException(status_code=404, detail="Country configuration not found")
    return db_config


