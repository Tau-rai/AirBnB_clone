#!/usr/bin/python3
"""This module defines the class Review which inherites from BaseModel """
from models.base_model import BaseModel


class Review(BaseModel):
    """
    Review class represents the review given by client

    Attributes:
        place_id: string - empty string: it will be the Place.id
        user_id: string - empty string: it will be the User.id
        text: string - empty string
    """
    place_id = ""
    user_id = ""
    text = ""
