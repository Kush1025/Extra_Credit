from sqlalchemy.orm import Session
from . import models, schemas

def create_survey(db: Session, survey: schemas.SurveyCreate):
    db_survey = models.StudentSurvey(**survey.dict())
    db.add(db_survey)
    db.commit()
    db.refresh(db_survey)
    return db_survey

def get_surveys(db: Session):
    return db.query(models.StudentSurvey).all()

def get_survey(db: Session, survey_id: int):
    return db.query(models.StudentSurvey).filter(models.StudentSurvey.id == survey_id).first()

def delete_survey(db: Session, survey_id: int):
    survey = get_survey(db, survey_id)
    if survey:
        db.delete(survey)
        db.commit()
    return survey

def update_survey(db: Session, survey_id: int, data: schemas.SurveyCreate):
    survey = get_survey(db, survey_id)
    if survey:
        for key, value in data.dict().items():
            setattr(survey, key, value)
        db.commit()
        db.refresh(survey)
    return survey
