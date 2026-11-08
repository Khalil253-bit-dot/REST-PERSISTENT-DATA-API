from pydantic import BaseModel, Field
import datetime


class ClinicalDataCreate(BaseModel):
    patient_name: str = Field(..., example="John Doe")
    age: int = Field(..., ge=0, le=120, example=45)
    diagnosis: str = Field(..., example="Hypertension")
    weightInLbs: int = Field(..., ge=0, example=180)
    race: str = Field(..., example="Caucasian")
    preExistingConditions: str = Field(None, example="Diabetes, Asthma")


# The read schema includes the auto-generated fields
class ClinicalDataRead(ClinicalDataCreate):
    id: int
    recorded_at: datetime.datetime
