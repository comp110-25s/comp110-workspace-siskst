"""File to define Bear class."""


class Bear:
    age: int
    hunger_score: int

    def __init__(self):
        self.age = 0
        self.hunger_score = 0
        return None

    def one_day(self):
        """Bear gets older and hungrier daily"""
        self.age += 1
        self.hunger_score -= 1

        return None

    # method for bear eating
    def eat(self, num_fish: int) -> None:
        self.hunger_score += num_fish
