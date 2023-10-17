from abc import ABC, abstractmethod


class Shape3d(ABC):
    @abstractmethod
    def volume(self):
        pass
