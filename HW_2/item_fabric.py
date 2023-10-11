from abc import ABC, abstractmethod


class ItemFabric(ABC):
    def __init__(self):
        self.game_item = None

    @abstractmethod
    def create_item(self):
        pass

    def open_reward(self):
        self.game_item = self.create_item()
        self.game_item.open()
