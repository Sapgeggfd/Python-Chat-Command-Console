from typing import Callable, override
from .command import Command
from .commadn_execeptions import MissingArgument


class GiveCommand(Command):
    name: str = "give"
    desc: str = "Gives a item to a player"

    def __init__(self, callback: Callable) -> None:
        super().__init__(callback=callback)

    @override
    def execute(self, *args, **kwargs) -> None:
        if player := kwargs.get("player"):
            if item := kwargs.get("item"):
                if self.callback:
                    self.callback(player=player, item=item)
        else:
            raise MissingArgument(missing_arg="player")
