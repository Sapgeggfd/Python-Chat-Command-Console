from typing import Callable, override
from .command import Command
from .commadn_execeptions import MissingArgument


class TeleportCommand(Command):
    name: str = "teleport"
    desc: str = "teleports player"
    alias:list[str] = ["tp"]

    def __init__(self, callback: Callable) -> None:
        super().__init__(callback=callback)

    @override
    def execute(self, *args, **kwargs) -> None:
        if player := kwargs.get("player"):
            if pos := kwargs.get("pos"):
                if self.callback:
                    self.callback(player=player, pos=pos)
        else:
            raise MissingArgument(missing_arg="player")
