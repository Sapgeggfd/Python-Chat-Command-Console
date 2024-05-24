class CommandRegistry:
    def __init__(self) -> None:
        self.commands = {}

    def register_command(self, command) -> None:
        self.commands[command.name] = command
        if "alias" in command.__dir__():
            for alias in command.alias:
                print(alias)
                self.commands[alias] = command

    def execute_command(self, name, *args, **kwargs) -> None:
        command = self.commands.get(name)
        if command:
            command.execute(*args, **kwargs)
        else:
            print(f"Unknown command: {name}")
