# TODO Написать 3 класса с документацией и аннотацией типов

from abc import ABC, abstractmethod

class Table(ABC):
    def __init__(self, color: str, material: str, height: float, width: float, length: float):
        if height <= 0 or width <= 0 or length <= 0:
            raise ValueError("Высота, ширина и длина должны быть положительными числами.")
        self.color = color
        self.material = material
        self.height = height
        self.width = width
        self.length = length

    @abstractmethod
    def set_on_table(self, item: str) -> str:
        ...

    @abstractmethod
    def clean_surface(self) -> str:
        ...

class Tree(ABC):
    def __init__(self, species: str, age: int, height: float):
        if age < 0:
            raise ValueError("Возраст не может быть отрицательным.")
        if height <= 0:
            raise ValueError("Высота должна быть положительным числом.")
        self.species = species
        self.age = age
        self.height = height

    @abstractmethod
    def grow(self) -> str:
        ...

    @abstractmethod
    def shed_leaves(self) -> str:
        ...

class SocialMedia(ABC):
    def __init__(self, name: str, user_count: int):
        if user_count < 0:
            raise ValueError("Количество пользователей не может быть отрицательным.")
        self.name = name
        self.user_count = user_count

    @abstractmethod
    def post_update(self, content: str) -> str:
        ...

    @abstractmethod
    def delete_account(self) -> str:
        ...

if __name__ == "__main__":
    pass

