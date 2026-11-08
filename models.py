from xmlrpc.client import Boolean

from sqlalchemy import Column, Integer, String, DateTime

import datetime
from database import Base


class ClinicalData(Base):
    __tablename__ = "clinical_data"

    id = Column(Integer, primary_key=True, index=True)
    patient_name = Column(String, nullable=False)
    age = Column(Integer, nullable=False)
    diagnosis = Column(String, nullable=False)
    recorded_at = Column(DateTime, default=datetime.datetime.utcnow)
    weightInLbs = Column(Integer, nullable=False)
    race = Column(String, nullable=False)
    preExistingConditions = Column(String, nullable=True)

    def to_dict(self):
        """Return a JSON‑serialisable dict representation."""
        return {
            "id": self.id,
            "patient_name": self.patient_name,
            "age": self.age,
            "diagnosis": self.diagnosis,
            "recorded_at": self.recorded_at.isoformat(),
            "weightInLbs": self.weightInLbs,
            "race": self.race,
            "preExistingConditions": self.preExistingConditions,
        }
