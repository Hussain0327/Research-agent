from __future__ import annotations

from typing import List, Optional, Dict
from pydantic import BaseModel, Field, HttpUrl


class FormInput(BaseModel):
    topic: str = Field(..., description="Newsletter topic")
    tone: str = Field(..., description="Newsletter tone, e.g., Professional, Funny")
    audience: str = Field(..., description="Target audience description")


class SectionPlan(BaseModel):
    title: str
    description: Optional[str] = ""


class PlanOutput(BaseModel):
    newsletterSections: List[SectionPlan] = Field(default_factory=list)


class SearchResult(BaseModel):
    url: HttpUrl
    title: Optional[str] = None
    content: Optional[str] = None


class SectionDraft(BaseModel):
    title: str
    html: str
    sources: List[HttpUrl] = Field(default_factory=list)


class Newsletter(BaseModel):
    subject: str
    html: str
    sources: Dict[str, str] = Field(
        default_factory=dict,
        description="Map of URL -> best-known title/name",
    )

