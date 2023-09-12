#!/usr/bin/python3
"""Define a class od student"""


class Student:
    def __init__(self, first_name, last_name, age):
        """
        Args:
            first_name: student's fisrt name
            last_name: student's last name
            age: student's age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

        def to_json(self):
            return self.__dict__
