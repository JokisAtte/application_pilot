from typing import List, Optional
from pydantic import BaseModel, Field

class WorkExperience(BaseModel):
    companyName: str
    startDate: str = Field(..., description="Format: YYYY-MM")
    endDate: Optional[str] = Field(None, description="Format: YYYY-MM or None for 'Present'")
    title: str
    description: str
    skills: List[str]

class PreviousApplicationStyleSample(BaseModel):
    title: Optional[str] = None
    companyName: Optional[str] = None
    applicationText: str
    jobDescription: Optional[str] = None # Added for context
    dateSent: str = Field(..., description="Format: YYYY-MM")

class DesiredFuture(BaseModel):
    targetRoles: List[str]
    preferredIndustries: List[str]
    locationPreference: str # e.g., "Remote", "Tampere", "Hybrid"
    keySellingPoints: List[str] # The "highlights" you want in every letter
    minSalary: Optional[int] = None