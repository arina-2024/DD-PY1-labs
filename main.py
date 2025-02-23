class Tree:
    def __init__(self, species: str, height: float, age: int) -> None:
        self.__species = species
        self.__height = height
        self.__age = age

    def get_info(self) -> str:
        return f'{self.__species}, высота: {self.__height} м, возраст: {self.__age} лет'

    def __str__(self) -> str:
        return f'{self.__species} (высота: {self.__height} м, возраст: {self.__age} лет)'

    def __repr__(self) -> str:
        return f'Tree(species="{self.__species}", height={self.__height}, age={self.__age})'


class Spruce(Tree):
    def __init__(self, height: float, age: int, needle_length: float) -> None:
        super().__init__('Ель', height, age)
        self.__needle_length = needle_length

    def get_info(self) -> str:
        return f'{super().get_info()}, длина иголок: {self.__needle_length} см'

    def __str__(self) -> str:
        return f'{super().__str__()} с длиной иголок {self.__needle_length} см'

    def __repr__(self) -> str:
        return f'Spruce(height={self._Tree__height}, age={self._Tree__age}, needle_length={self.__needle_length})'


class Pine(Tree):
    def __init__(self, height: float, age: int, cone_count: int) -> None:
        super().__init__('Сосна', height, age)
        self.__cone_count = cone_count

    def get_info(self) -> str:
        return f'{super().get_info()}, количество шишек: {self.__cone_count}'

    def __str__(self) -> str:
        return f'{super().__str__()} с количеством шишек {self.__cone_count}'

    def __repr__(self) -> str:
        return f'Pine(height={self._Tree__height}, age={self._Tree__age}, cone_count={self.__cone_count})'


if __name__ == "__main__":
    spruce = Spruce(10.5, 15, 5)
    pine = Pine(12.0, 20, 30)

    print(spruce)
    print(repr(spruce))
    print(spruce.get_info())

    print(pine)
    print(repr(pine))
    print(pine.get_info())

