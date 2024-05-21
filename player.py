import uuid


class Player:
    id: uuid.UUID
    name: str

    def __init__(self, name: str) -> None:
        self.id = uuid.uuid4()
        self.name = name
