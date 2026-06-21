import random
from typing import override


class Plane:

    def __init__(self, name="default plane name"):
        # __ just hides the data member from the user.
        self.name = name
        self.__x = 0
        self.__y = 0

    def update_position(self):
        self.__x += random.randint(-1, 1)
        self.__y += random.randint(-1, 1)

    def get_position(self):
        return self.__x, self.__y

    # overrides __str__ method
    @override
    def __str__(self):
        return '"{}" is in: ({}, {}).'.format(self.name, self.__x, self.__y)
