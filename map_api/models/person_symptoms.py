"""MODELS - PERSON SYMPTOMS
The symptoms of a person is part of the Person model
"""

# # Native # #
from datetime import date
from typing import Optional
from contextlib import suppress

# # Package # #
from .common import BaseModel
from .fields import SymptomFields

__all__ = ("Symptoms", )


class Symptoms(BaseModel):
    """The symptoms information of a person"""
    q1: str = SymptomFields.q1
    q2: str = SymptomFields.q2
    q3: str = SymptomFields.q3
    q4: str = SymptomFields.q4
    q5: str = SymptomFields.q5
    q6: str = SymptomFields.q6
    q7: str = SymptomFields.q7
    q8: str = SymptomFields.q8
    q9: str = SymptomFields.q9
    q10: str = SymptomFields.q10
    created: Optional[date] = SymptomFields.created
    updated: Optional[date] = SymptomFields.updated

    def dict(self, **kwargs):
        # The "birth" field must be converted to string (isoformat) when exporting to dict (for Mongo)
        # TODO Better way to do this? (automatic conversion can be done with Config.json_encoders, but not available for dict
        d = super().dict(**kwargs)
        with suppress(KeyError):
            d["created"] = d.pop("created").isoformat()
            d["updated"] = d.pop("updated").isoformat()
        return d
