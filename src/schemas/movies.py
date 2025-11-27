from datetime import date
from typing import Optional, List
from enum import Enum
from pydantic import BaseModel
from database.models import MovieStatusEnum


class ORMBaseModel(BaseModel):
    class Config:
        from_attributes = True


class Genre(BaseModel):
    id: int
    name: str


class Actor(BaseModel):
    id: int
    name: str


class Country(BaseModel):
    id: int
    code: str
    name: str | None


class Language(BaseModel):
    id: int
    name: str


class Movie(BaseModel):
    name: str
    date: date
    score: float
    overview: Optional[str] = None
    status: MovieStatusEnum
    budget: float
    revenue: float
    country: Country
    genres: List[Genre]
    actors: List[Actor]
    languages: List[Language]


class MovieDetail(Movie, ORMBaseModel):
    id: int


class MovieUpdate(ORMBaseModel):
    name: Optional[str] = None
    date: Optional[date] = None
    score: Optional[float] = None
    overview: Optional[str] = None
    status: Optional[MovieStatusEnum] = None
    budget: Optional[float] = None
    revenue: Optional[float] = None


class MovieCreate(ORMBaseModel):
    name: str
    date: date
    score: float
    overview: str
    status: MovieStatusEnum
    budget: float
    revenue: float
    country: str
    genres: list[str]
    actors: list[str]
    languages: list[str]


class MovieList(ORMBaseModel):
    id: int
    name: str
    date: date
    score: float
    overview: Optional[str] = None


class MovieListPagination(BaseModel):
    movies: List[MovieList]
    prev_page: Optional[str]
    next_page: Optional[str]
    total_pages: int
    total_items: int
