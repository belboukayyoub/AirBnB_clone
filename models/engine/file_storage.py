#!/usr/bin/python3
"""
module defines a class that handles file storage of all class instances.
"""
import json


class FileStorage:
    """handles file storage of all class instances"""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Return the dictionary __objects."""
        return FileStorage.__objects

    def new(self, obj):
        """Set in __objects obj with key <obj_class_name>.id"""
        obj_class_name = obj.__class__.__name__
        FileStorage.__objects["{}.{}".format(obj_class_name, obj.id)] = obj

    def save(self):
        """Serialize __objects to the JSON file __file_path."""
        _dict = FileStorage.__objects
        objdict = {obj: _dict[obj].to_dict() for obj in _dict.keys()}
        with open(FileStorage.__file_path, "w") as file:
            json.dump(objdict, file)

    def reload(self):
        """Deserialize the JSON file __file_path to __objects, if it exists."""
        try:
            with open(FileStorage.__file_path) as file:
                _dict = json.load(file)
                for obj in _dict.values():
                    self.new(self.__new_class(obj))
        except FileNotFoundError:
            return

    def __new_class(self, _dict):
        """Create new object"""

        _obj = self.classes()[_dict["__class__"]](**_dict)
        return _obj

    def classes(self):
        """Create new object"""
        from models.base_model import BaseModel
        from models.user import User
        from models.amenity import Amenity
        from models.city import City
        from models.place import Place
        from models.review import Review
        from models.state import State

        return {
            "BaseModel": BaseModel,
            "User": User,
            "Amenity": Amenity,
            "City": City,
            "Place": Place,
            "Review": Review,
            "State": State,
        }
