from example_commands import give, teleport
from example_commands.command_callbacks import give_player_item, tp_player
from item import Item
from player import Player
from pygchat.commandregistry import CommandRegistry
from pygchat.commands import help

command_registry: CommandRegistry = CommandRegistry()

player1: Player = Player(name="Player1")
item_dirt: Item = Item(itemID="dirt", display_name="Dirt")


def register_commands() -> None:

    command_registry.register_command(command=help.HelpCommand(command_registry=command_registry))
    command_registry.register_command(command=give.GiveCommand(callback=give_player_item))
    command_registry.register_command(command=teleport.TeleportCommand(callback=tp_player))


def execute_commands() -> None:

    command_registry.execute_command(name="help")
    command_registry.execute_command(name="give", player=player1, item=item_dirt)
    command_registry.execute_command(name="teleport", player=player1, pos=(10, 10))


def main() -> None:
    register_commands()
    execute_commands()


if __name__ == "__main__":
    main()
