from item_fabric import ItemFabric
from silver_reward import SilverReward


class SilverGenerator(ItemFabric):
    def create_item(self):
        print('New breast created.')
        return SilverReward()
