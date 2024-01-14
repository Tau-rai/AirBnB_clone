#!/usr/bin/python3
"""This module defines a class User that represents a user entity."""

from models.base_model import BaseModel


class User(BaseModel):
    """
    User class represents the user.

    Attributes:
        email (str): Email address of the user.
        password (str): Password associated with the user's account.
        first_name (str): First name of the user.
        last_name (str): Last name of the user.
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
