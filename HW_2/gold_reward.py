from i_game_item import IGameItem


class GoldReward(IGameItem):
    def open(self):
        print('Gold')
