from typing import Callable, Optional


class Command:
    name: str
    desc: str
    alias: list[str]
    callback: Optional[Callable]

    def __init__(self, callback: Optional[Callable] = None) -> None:
        self.callback = callback

    def execute(self, command_registry, *args):
        raise NotImplementedError("You should implement this method!")
