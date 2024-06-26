#!/usr/bin/python3
"""File storage class"""
import json
import os


class FileStorage:
    """This class Serializes/Deserializes JSON files"""

    __file_path = 'file.json'
    __objects = {}

    def all(self, cls=None):
        """
        Returns the dictionary representation of __objects
        It also returns object of a specific class  if 'cls' is not None
        """
        if cls is not None:
            objs = {}
            if isinstance(cls, str):
                cls = eval(cls)

            for key, value in self.__objects.items():
                if isinstance(value, cls):
                    objs[key] = value
            return objs

        return self.__objects

    def new(self, obj):
        """
        sets in __objects the obj with key <obj class name>.id
        """
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """Serializes __object to the JSON file"""
        serialized_obj = {}
        for key, value in self.__objects.items():
            serialized_obj[key] = value.to_dict()

        with open(self.__file_path, 'w', encoding='utf-8') as json_file:
            json.dump(serialized_obj, json_file, indent=4)

    def reload(self):
        """
        Deserializes the JSON file to __objects
        (only if the JSON file __file_path exists)
        """
        if os.path.exists(self.__file_path):
            with open(self.__file_path, 'r', encoding='utf-8') as json_file:
                data = json.load(json_file)
                for key, value in data.items():
                    class_name, obj_id = key.split('.')
                    if class_name == 'BaseModel':
                        cls_name = 'base_model'
                    else:
                        cls_name = class_name.lower()

                    module = __import__(f'models.{cls_name}',
                                        fromlist=[class_name])
                    cls = getattr(module, class_name)
                    self.__objects[key] = cls(**value)

    def delete(self, obj=None):
        """
        This method deletes an object passed to it  and does nothing
        if the object passed to it is None
        """

        if obj is not None:
            key = f"{type(obj).__name__}.{obj.id}"
            del self.__objects[key]

    def close(self):
        """
        This method calls reload() method for deseializing the JSON
        file to objects
        """
        self.reload()
