from typing import Protocol


class Item(Protocol):
    itemID: str


class Player(Protocol):
    _pos: tuple[int, int]

    @property
    def pos(self) -> tuple[int, int]: ...
    @pos.setter
    def pos(self, value: tuple[int, int]) -> None: ...
    def add_item(self, item: Item): ...
