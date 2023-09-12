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

        def to_json(self, attrs=None):
            """Get a dictionary representation of the Student.

            If attrs is a list of strings, represents only those attributes
            included in the list.

            Args:
            attrs (list): (Optional) The attributes to represent.
            """
            if (type(attrs) == list and
                    all(type(ele) == str for ele in attrs)):
                return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
            return self.__dict__
