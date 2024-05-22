from chat import Chat
import commands.give
import commands.help
import commands.teleport
from item import Item
from player import Player
from commandregistry import CommandRegistry
import commands
from command_callbacks import give_player_item, tp_player

player1 = Player(name="Player1")
player2 = Player(name="Player2")

item_dirt = Item(itemID="dirt", display_name="Dirt")
item_stone = Item(itemID="stone", display_name="Stone")


def register_commands(command_registry: CommandRegistry) -> None:
    cr = command_registry

    cr.register_command(command=commands.help.HelpCommand(command_registry=cr))
    cr.register_command(command=commands.give.GiveCommand(callback=give_player_item))
    cr.register_command(command=commands.teleport.TeleportCommand(callback=tp_player))


def eacute_commands(command_registry: CommandRegistry):
    cr = command_registry
    cr.execute_command(name="help")
    cr.execute_command(name="give", player=player1, item=item_stone)
    cr.execute_command(name="teleport", player=player1, pos=(10, 10))


def chat_helloworld(chat: Chat):
    chat.add_character(character="H")
    chat.add_character(character="a")
    chat.add_character(character="l")
    chat.add_character(character="l")
    chat.add_character(character="o")
    # chat.add_character(" ")
    chat.add_character(character="W")
    chat.add_character(character="o")
    chat.add_character(character="r")
    chat.add_character(character="l")
    chat.add_character(character="d")

    print(chat.current_input)
    chat.cursor_pos = 5
    chat.insert_character_on_cursor_pos(character=" ")
    print(chat.current_input)


def main() -> None:
    chat = Chat(player=player1)
    register_commands(command_registry=chat.command_registry)

    eacute_commands(command_registry=chat.command_registry)


if __name__ == "__main__":
    main()
