from abc import ABC, abstractmethod


class User:
    def __init__(self, id: int, name: str, hash_pass: int, account: int):
        self.id = id
        self.name = name
        self.hash_pass = hash_pass
        self.account = account


class IUserRepo(ABC):
    @abstractmethod
    def create(self, user: User) -> bool:
        pass

    @abstractmethod
    def get(self, name: str) -> User:
        pass

    @abstractmethod
    def delete(self, user: User) -> bool:
        pass


class UserRepository(IUserRepo):
    def __init__(self):
        self.repo = [User]

    def create(self, name: str) -> bool:
        pass

    def get(self, name: str) -> User:
        pass

    def delete(self, user: User) -> bool:
        pass


class UserProvider:
    def __init__(self):
        self.user_repo = UserRepository()

    def register(self, name: str) -> bool:
        if self.user_repo.create(name):
            return True
        return False

    def get_user(self, name: str) -> User:
        return self.user_repo.get(name)
