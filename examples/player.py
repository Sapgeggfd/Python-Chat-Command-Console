import uuid

from pygchat.helper_protocols import Item


class Player:
    id: uuid.UUID
    name: str
    _pos: tuple[int, int]
    inventory: dict[object, int]

    @property
    def pos(self) -> tuple[int, int]:
        return self.pos

    @pos.setter
    def pos(self, value: tuple[int, int]) -> None:
        self._pos = value
        print(f"new_pos: {self._pos}")

    def __init__(self, name: str) -> None:
        self.id = uuid.uuid4()
        self.name = name
        self._pos = (0, 0)
        self.inventory = {}

    def add_item(self, item: Item) -> None:
        print(f"{self.name} received {item.itemID}")
        if item in self.inventory:
            self.inventory[item] += 1
        else:
            self.inventory[item] = 1
