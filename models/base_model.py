#!/usr/bin/python3
"""
base class for the airbnb project
"""
from datetime import datetime
from uuid import uuid4
import models

class BaseModel:
    """Custom base for classes in AirBnB project

    Arttributes:
        id(str): user id.
        created_at: to assign current datetime.
        updated_at: to update current datetime.
    Methods:
        __str__: prnt the classname -id - creates dict representations of the input val.
        save(self): update current datetime.
        to_dict(self): returns the dict values for instance object.

    """

    def __init__(self, *args, **kwargs):
        """Public instance artributes initialization after creation

        Args:
            *args(args): args
            **kwargs(dict): attribute val

        """
        DATE_TIME_FORMAT = '%Y-%m-%dT%H:%M:%S.%f'
        if not kwargs:
            self.id = str(uuid4())
            self.created_at = datetime.utcnow()
            self.updated_at = datetime.utcnow()
            models.storage.new(self)
        else:
            for key, value in kwargs.items():
                if key in ("updated_at", "created_at"):
                    self.__dict__[key] = datetime.strptime(
                        value, DATE_TIME_FORMAT)
                elif key[0] == "id":
                    self.__dict__[key] = str(value)
                else:
                    self.__dict__[key] = value

    def __str__(self):
        """
        Return string representation of class
        """
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__)

    def save(self):
        """
        Updates the public instance attribute
        """
        self.updated_at = datetime.utcnow()
        models.storage.save()

    def to_dict(self):
        """
        Method returns a dictionary containing all 
        """
        map_objects = {}
        for key, value in self.__dict__.items():
            if key == "created_at" or key == "updated_at":
                map_objects[key] = value.isoformat()
            else:
                map_objects[key] = value
        map_objects["__class__"] = self.__class__.__name__
        return map_objects