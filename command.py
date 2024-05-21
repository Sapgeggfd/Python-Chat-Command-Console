from player import Player
from typing import Callable


class Command:
    player: Player
    keyword: str
    execute_func: Callable

    def __init__(self, player: Player) -> None:
        self.player = player
