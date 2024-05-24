from pygchat.commandregistry import CommandRegistry
from pygchat.helper_protocols import Player


class Chat:
    player: Player  # Reference to the game Player Object

    _curser_pos: int
    _history: list[list[str]]
    _current_input: list[str]

    command_registry: CommandRegistry  # list of all registered commands
    _command_prefix: str

    autocomplete_hints: list

    ##############
    # Properties #
    ##############

    @property
    def cursor_pos(self) -> int:
        return self._curser_pos

    @cursor_pos.setter
    def cursor_pos(self, new_cursor_pos: int) -> None:
        l = len(self._current_input)
        if new_cursor_pos > l:
            self._curser_pos = l
        elif new_cursor_pos <= 0:
            self._curser_pos = 0
        else:
            self._curser_pos = new_cursor_pos

    #####################
    # End of Properties #
    #####################

    def __init__(
        self, issuer: Player, command_prefix="/", command_registry: CommandRegistry = CommandRegistry()
    ) -> None:
        # Game
        self.player = issuer

        # Chat System
        self._curser_pos = 0
        self._history = []
        self._current_input = []

        # Command Stuff
        self._command_prefix = command_prefix
        self.command_registry = command_registry

    def insert_character(self, character: str, pos=None) -> None:
        if pos:
            self._current_input.insert(pos, character)
        else:
            self._current_input.insert(self.cursor_pos, character)
        self.cursor_pos += 1

    def get_input(self) -> str:
        self._history.append(self._current_input)
        ret: list[str] = self._current_input
        self._current_input = []
        return "".join(ret)

    def remove_character(self): ...
    def add_command(self, command): ...

    def autocomplete(self): ...
