class Item:
    itemID: str
    display_name: str
    mod: str  # the mod the item is from (can be game)

    def __init__(self, itemID: str, display_name: str = "", mod: str = "game") -> None:
        self.itemID = itemID
        self.display_name = display_name
        self.mod = mod
