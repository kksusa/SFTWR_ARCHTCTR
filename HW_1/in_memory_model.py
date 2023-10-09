from model_elements import PoligonalModel, Flash, Camera, Scene, Poligon, Texture
from abc import ABC, abstractmethod


class IModelChangedObserver(ABC):
    @abstractmethod
    def apply_update_model(self):
        pass


class IModelChanger(ABC):
    @abstractmethod
    def notify_change(self, sender):
        pass


class ModelStore(IModelChanger):
    def __init__(self, models: [PoligonalModel], scenes: [Scene], flashes: [Flash], camera: [Camera],
                 change_observers: [IModelChangedObserver]):
        self.models = models
        self.models.append(PoligonalModel([Poligon], [Texture]))
        self.scenes = scenes
        self.scenes.append(Scene([PoligonalModel], [Flash], [Camera]))
        self.flashes = flashes
        self.flashes.append(Flash())
        self.camera = camera
        self.camera.append(Camera())
        self.__change_observers = change_observers

    def get_scena(self, num: int) -> Scene:
        return Scene([PoligonalModel], [Flash], [Camera])

    def notify_change(self, sender: IModelChanger):
        return sender