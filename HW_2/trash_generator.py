from item_fabric import ItemFabric
from trash_reward import TrashReward


class TrashGenerator(ItemFabric):
    def create_item(self):
        print('New breast created.')
        return TrashReward()
