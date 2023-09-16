import json
import csv
import turtle

class Base:
    """
    the base of the project
    Private Class Attributes:
        __nb_object (int): Number of Bases
    """
    __nb_objects = 0
    def __init__(self, id=None):
        
        """
        initialize new base
        Args:
            id: the id of the base
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
