from sqlalchemy import Column, Integer, String, Date
from .database import Base

class StudentSurvey(Base):
    __tablename__ = "student_survey"

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    street_address = Column(String, nullable=False)
    city = Column(String, nullable=False)
    state = Column(String, nullable=False)
    zip = Column(String, nullable=False)
    phone = Column(String, nullable=False)
    email = Column(String, nullable=False)
    survey_date = Column(Date, nullable=False)
    liked_most = Column(String)
    interested_reason = Column(String)
    recommendation_likelihood = Column(String)
