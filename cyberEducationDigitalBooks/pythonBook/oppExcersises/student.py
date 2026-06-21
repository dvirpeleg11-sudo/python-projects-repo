from typing_extensions import override
import person


class Student(person.Person):

    def __init__(self, name: str, age: int, is_excellent: bool):
        super().__init__(name, age)
        self.__is_excellent = is_excellent

    def is_excellent(self) -> bool:
        return self.__is_excellent

    @override
    def get_age(self) -> int:
        return self._age + 1

