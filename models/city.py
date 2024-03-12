#!/usr/bin/python3
"""
City class
"""
from models.base_model import BaseModel
class City(BaseModel):
    """class for city in project.

    Attributes:
        state_id (string): state id.
        name (string): city name.

    """

    state_id = ""
    name = ""
