#!/usr/bin/python3


class LockedClass:
    """
    allows only attr with name first_name
    """
    __slots__ = ["first_name"]
