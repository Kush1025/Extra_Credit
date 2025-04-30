from pydantic import BaseModel
from datetime import date

class SurveyBase(BaseModel):
    first_name: str
    last_name: str
    street_address: str
    city: str
    state: str
    zip: str
    phone: str
    email: str
    survey_date: date
    liked_most: str
    interested_reason: str
    recommendation_likelihood: str

class SurveyCreate(SurveyBase):
    pass

class Survey(SurveyBase):
    id: int
    class Config:
        orm_mode = True
