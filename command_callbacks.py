
from item import Item
from player import Player

def give_player_item(player: Player, item: Item) -> None:
    player.add_item(item=item)


def tp_player(player: Player, pos: tuple[int, int]) -> None:
    player.pos = pos