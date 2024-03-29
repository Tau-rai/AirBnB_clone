#!/usr/bin/python3
"""This module defines the class amenity that inherits from BaseModel"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """
    Amenity class represents a specific amenity.

    Attributes:
        name (str): The name of the amenity.
    """

    name = ""
