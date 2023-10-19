#!/usr/bin/python3
"""module defines a base class for all other classes to inherit from."""

import uuid
from datetime import datetime
from models import storage


class BaseModel:
    """Class for all other classes to inherit from."""

    def __init__(self, *args, **kwargs):
        """Initialize a BaseModel instance.

        Args:
                - *args (any): Unused
                - **kwargs (dict): dict of key-values arguments
        """
        if kwargs:
            time_format = '%Y-%m-%dT%H:%M:%S.%f'
            for key, val in kwargs.items():
                if key == '__class__':
                    continue
                elif key == 'created_at' or key == 'updated_at':
                    setattr(self, key, datetime.strptime(val, time_format))
                else:
                    setattr(self, key, val)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def save(self):
        """Update the public instance attribute
        updated_at with the current datetime."""

        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """
        Return a dictionary containing
        all keys/values of __dict__ of the instance.

        Returns:
            dict: A dictionary representation of the object.
        """

        obj_dict = self.__dict__.copy()
        obj_dict["created_at"] = self.created_at.isoformat()
        obj_dict["updated_at"] = self.updated_at.isoformat()
        obj_dict["__class__"] = self.__class__.__name__
        return obj_dict

    def __str__(self):
        """Return a string representation of the object."""

        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"
