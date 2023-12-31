#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
from models import storage
from models.city import City


class State(BaseModel):
    """ State class """
    name = ""

    def __init__(self, *args, **kwargs):
        """Instantiates a new State"""
        super().__init__(*args, **kwargs)

    def cities(self):
        """Returns the list of City objects linked to the current State"""
        city_list = []
        if storage.__class__.__name__ != 'DBStorage':
            for city in storage.all(City).values():
                if city.state_id == self.id:
                    city_list.append(city)
        return city_list
