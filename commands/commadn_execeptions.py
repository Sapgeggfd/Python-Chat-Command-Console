class CommandBaseException(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)

class MissingArgument(CommandBaseException):
    def __init__(self, *args: object,missing_arg = None) -> None:
        super().__init__(*args)
        self.missing_arg = missing_arg