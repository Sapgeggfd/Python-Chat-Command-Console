import pygchat.commands
import pygchat.commands.give
import pygchat.commands.help
import pygchat.commands.teleport
from command_callbacks import give_player_item, tp_player
from commandregistry import CommandRegistry
from item import Item
from player import Player
from pygchat.chat import Chat

player1 = Player(name="Player1")
player2 = Player(name="Player2")

item_dirt = Item(itemID="dirt", display_name="Dirt")
item_stone = Item(itemID="stone", display_name="Stone")


def register_commands(command_registry: CommandRegistry) -> None:
    cr = command_registry

    cr.register_command(command=pygchat.commands.help.HelpCommand(command_registry=cr))
    cr.register_command(command=pygchat.commands.give.GiveCommand(callback=give_player_item))
    cr.register_command(command=pygchat.commands.teleport.TeleportCommand(callback=tp_player))


def eacute_commands(command_registry: CommandRegistry):
    cr = command_registry
    cr.execute_command(name="help")
    cr.execute_command(name="give", player=player1, item=item_stone)
    cr.execute_command(name="teleport", player=player1, pos=(10, 10))


def chat_helloworld(chat: Chat):

    txt = "HelloWorld"
    for char in txt:
        chat.insert_character(character=char)

    chat.insert_character(character=" ", pos=5)
    print(chat.get_input())
    txt = "Hey Sapge"
    for char in txt:
        chat.insert_character(character=char)
    print(chat.get_input())
    print(chat._history)


def main() -> None:
    chat = Chat(player=player1)
    register_commands(command_registry=chat.command_registry)

    chat_helloworld(chat)

    # eacute_commands(command_registry=chat.command_registry)


if __name__ == "__main__":
    main()
