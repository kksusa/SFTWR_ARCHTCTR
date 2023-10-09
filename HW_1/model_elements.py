class Point3D:
    pass


class Angle3D:
    pass


class Color:
    pass


class Type:
    pass


class Poligon:
    def __init__(self, points: [Point3D]):
        self.points = points


class Texture:
    pass


class PoligonalModel:
    def __init__(self, poligons: [Poligon], textures: [Texture]):
        self.poligons = poligons
        self.poligons.append(Poligon([Point3D]))
        self.textures = textures


class Flash:
    def __init__(self):
        self.location = Point3D()
        self.angle = Angle3D()
        self.color = Color()
        self.power = float()

    def rotate(self, angle3d):
        pass

    def move(self, point3d):
        pass


class Camera:
    def __init__(self):
        self.location = Point3D()
        self.angle = Angle3D()

    def rotate(self, angle3d: Angle3D):
        pass

    def move(self, point3d: Point3D):
        pass


class Scene:
    def __init__(self, models: [PoligonalModel], flash: [Flash], camera: [Camera]):
        self.id = int()
        self.models = models
        self.models.append(PoligonalModel([Poligon], [Texture]))
        self.flashes = flash
        self.camera = camera
        self.camera.append(Camera)

    def method1(self, type: Type) -> Type:
        return type

    def method2(self, type_1: Type, type_2: Type) -> Type:
        return type_1
