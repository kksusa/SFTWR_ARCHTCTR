from item_fabric import ItemFabric
from gold_reward import GoldReward


class GoldGenerator(ItemFabric):
    def create_item(self):
        print('New breast created.')
        return GoldReward()
