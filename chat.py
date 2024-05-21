from typing import Any, Callable, LiteralString, Optional
from player import Player


class Chat:
    player: Player  # Reference to the game Player Object

    _curser_pos: int
    _history: list[str]
    _current_input: list

    _commands: list  # list of all registered commands
    _command_prefix: str

    autocomplete_hints: list

    ##############
    # Properties #
    ##############

    @property
    def cursor_pos(self) -> int:
        return self._curser_pos

    @cursor_pos.setter
    def cursor_pos(self, value) -> None:
        self._curser_pos = value

    @property
    def current_input(self) -> LiteralString:
        return "".join(self._current_input)

    #####################
    # End of Properties #
    #####################

    def __init__(self, player: Player, command_prefix="/") -> None:
        # Game
        self.player = player

        # Chat System
        self._curser_pos = 0
        self._history = []
        self._current_input = []

        # Command Stuff
        self._command_prefix = command_prefix
        self.autocomplete_hints = []

    def insert_character_on_cursor_pos(self, character: str) -> None:
        self._current_input.insert(self.cursor_pos, character)

    def add_character(self, character: str) -> None:
        self._current_input.append(character)
        self.cursor_pos += 1

    def remove_character(self): ...
    def add_command(self, command): ...

    def autocomplete(self): ...


# /give <?@player> <mod:itemID> <?amount> <?data>
# /teleport <?@player> <?dimension> <pos>





class GiveCommand(Command):
    def __init__(self, player: Player) -> None:
        super().__init__(player=player)
        self.keyword = "give"
        self.execute_func = give_item


def give_item(player, item, amount, data):
    print(f"gave {player.name} {item} ")
