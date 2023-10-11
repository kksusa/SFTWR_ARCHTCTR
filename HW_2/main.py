from random import choice
from gold_generator import GoldGenerator
from gem_generator import GemGenerator
from silver_generator import SilverGenerator
from trash_generator import TrashGenerator


if __name__ == '__main__':
    lst = [GoldGenerator(), GemGenerator(), SilverGenerator(), TrashGenerator()]
    for i in range(20):
        choice(lst).open_reward()
