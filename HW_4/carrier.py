from abc import ABC, abstractmethod


class Carrier:
    def __init__(self, id: int, name: str, places: int, account: int):
        self.id = id
        self.name = name
        self.places = places
        self.free_places = places
        self.account = account


class ICarrierRepo(ABC):
    @abstractmethod
    def add(self, user: Carrier) -> bool:
        pass

    @abstractmethod
    def get(self, name: str) -> Carrier:
        pass

    @abstractmethod
    def delete(self, carrier: Carrier) -> bool:
        pass


class CarrierRepository(ICarrierRepo):
    def __init__(self):
        self.repo = [Carrier]

    def add(self, name: str) -> bool:
        pass

    def get(self, name: str) -> Carrier:
        pass

    def delete(self, carrier: Carrier) -> bool:
        pass


class CarrierProvider:
    def __init__(self):
        self.carrier_repo = CarrierRepository()

    def add_carrier(self, carrier: Carrier) -> bool:
        if self.carrier_repo.add(carrier):
            return True
        return False

    def booking_ticket(self, carrier: Carrier, value: int) -> bool:
        for item in self.carrier_repo.repo:
            if item.id == carrier.id:
                if item.free_places >= value:
                    item.free_places -= value
                    return True
        return False

    def return_ticket(self, carrier: Carrier, value: int) -> bool:
        for item in self.carrier_repo.repo:
            if item.id == carrier.id:
                if item.free_places + value <= item.places:
                    item.free_places += value
                    return True
        return False
