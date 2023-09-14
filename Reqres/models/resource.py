from typing import List
from pydantic import BaseModel, HttpUrl, Field


class Support(BaseModel):
    url: str
    text: str


class Data(BaseModel):
    id: int
    name: str
    year: int
    color: str
    pantone_value: str


class ResponseData(BaseModel):
    data: Data
    support: Support


class Color(BaseModel):
    id: int
    name: str
    year: int
    color: str
    pantone_value: str


class ResponseDataList(BaseModel):
    page: int
    per_page: int
    total: int
    total_pages: int
    data: List[Color]
    support: Support
