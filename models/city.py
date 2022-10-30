#!/usr/bin/python3
''' City class module '''

from models.base_model import BaseModel


class City(BaseModel):
    ''' City class inherits BaseModel '''

    state_id = ""
    name = ""
