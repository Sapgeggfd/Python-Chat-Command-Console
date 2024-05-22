from .command import Command


class HelpCommand(Command):
    name: str = "help"
    desc: str = "Shows all available commands"
    def __init__(self,command_registry) -> None:
        self.command_registry = command_registry

    def execute(self, *args,**kwargs) -> None:
        output = []
        for name,com in self.command_registry.commands.items():
            output.append(name)
            output.append(f"\t{com.desc}")
        print(f"Available commands:\n{"\n".join(output)}")
