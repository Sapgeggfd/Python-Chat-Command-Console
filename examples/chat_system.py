from player import Player
from pygchat.chat import Chat

player1 = Player(name="Player1")
chat = Chat(player=player1)


def insert_text_to_chat(txt: str) -> None:
    for char in txt:
        chat.insert_character(character=char)


def main() -> None:
    insert_text_to_chat(txt="Hello PyGChat")
    print(chat.get_input())
    insert_text_to_chat(txt="Lorem Ipsum")
    print(chat.get_input())
    print(chat._history)


if __name__ == "__main__":
    main()
