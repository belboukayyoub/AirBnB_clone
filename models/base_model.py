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
        time_format = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = self.created_at
        if kwargs is not None and kwargs != {}:
            for key in kwargs:
                if key == "created_at":
                    self.__dict__["created_at"] = datetime.strptime(
                        kwargs["created_at"], time_format
                    )
                elif key == "updated_at":
                    self.__dict__["updated_at"] = datetime.strptime(
                        kwargs["updated_at"], time_format
                    )
                elif key == "__class__":
                    continue
                else:
                    self.__dict__[key] = kwargs[key]
        else:
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
