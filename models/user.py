#!/usr/bin/python3
"""
User class.
"""
from models.base_model import BaseModel

class User(BaseModel):
    """Represent a User

    Attributes:
        email (str): user email
        password (str): user password
        first_name (str): first name
        last_name (str): last name

    """
    first_name = ""
    last_name = ""
    email = ""
    password = ""

