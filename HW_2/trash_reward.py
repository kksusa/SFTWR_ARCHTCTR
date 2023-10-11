from i_game_item import IGameItem


class TrashReward(IGameItem):
    def open(self):
        print('Trash')
