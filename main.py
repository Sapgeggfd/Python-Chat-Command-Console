from chat import Chat


def main() -> None:
    chat = Chat()
    
    
    chat.add_character("H")
    chat.add_character("a")
    chat.add_character("l")
    chat.add_character("l")
    chat.add_character("o")
    # chat.add_character(" ")
    chat.add_character("W")
    chat.add_character("o")
    chat.add_character("r")
    chat.add_character("l")
    chat.add_character("d")

    print(chat.current_input)
    chat.cursor_pos = 5
    chat.insert_character_on_cursor_pos(" ")
    print(chat.current_input)

if __name__ == "__main__":
    main()
