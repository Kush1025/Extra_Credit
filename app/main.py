from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from . import crud, models, schemas
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/surveys/", response_model=schemas.Survey)
def create(survey: schemas.SurveyCreate, db: Session = Depends(get_db)):
    return crud.create_survey(db, survey)

@app.get("/surveys/", response_model=list[schemas.Survey])
def read_all(db: Session = Depends(get_db)):
    return crud.get_surveys(db)

@app.get("/surveys/{survey_id}", response_model=schemas.Survey)
def read_one(survey_id: int, db: Session = Depends(get_db)):
    survey = crud.get_survey(db, survey_id)
    if not survey:
        raise HTTPException(status_code=404, detail="Survey not found")
    return survey

@app.put("/surveys/{survey_id}", response_model=schemas.Survey)
def update(survey_id: int, survey: schemas.SurveyCreate, db: Session = Depends(get_db)):
    return crud.update_survey(db, survey_id, survey)

@app.delete("/surveys/{survey_id}")
def delete(survey_id: int, db: Session = Depends(get_db)):
    result = crud.delete_survey(db, survey_id)
    if not result:
        raise HTTPException(status_code=404, detail="Survey not found")
    return {"message": "Deleted successfully"}
