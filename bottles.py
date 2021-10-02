from __future__ import annotations


class BottleNumber(object):
    def __init__(self, number: int) -> None:
        self.number = number

    @staticmethod
    def factory(number: int) -> BottleNumber:
        if number == 0:
            return BottleNumber0(number)
        elif number == 1:
            return BottleNumber1(number)
        elif number == 6:
            return BottleNumber6(number)
        else:
            return BottleNumber(number)

    @property
    def quantity(self) -> str:
        return str(self.number)

    @property
    def successor(self) -> BottleNumber:
        return self.factory(self.number - 1)

    @property
    def pronoun(self) -> str:
        return "one"

    @property
    def container(self) -> str:
        return "bottles"

    @property
    def action(self) -> str:
        return f"Take {self.pronoun} down and pass it around, "

    def __str__(self) -> str:
        return f"{self.quantity} {self.container}"


class BottleNumber0(BottleNumber):
    @property
    def quantity(self) -> str:
        return "no more"

    @property
    def successor(self) -> BottleNumber:
        return self.factory(99)

    @property
    def action(self) -> str:
        return "Go to the store and buy some more, "


class BottleNumber1(BottleNumber):
    @property
    def pronoun(self) -> str:
        return "it"

    @property
    def container(self) -> str:
        return "bottle"


class BottleNumber6(BottleNumber):
    @property
    def quantity(self):
        return "1"

    @property
    def container(self):
        return "six-pack"


class Bottles(object):
    def verse(self, number: int) -> str:
        if number < 0 or number > 99:
            raise IndexError("The verse number N should be 0 <= N <= 99.")

        bottle_number = BottleNumber.factory(number)

        return f"{bottle_number} of beer on the wall, ".capitalize() + \
               f"{bottle_number} of beer.\n" + \
               f"{bottle_number.action}" + \
               f"{bottle_number.successor} of beer on the wall.\n"

    def song(self) -> str:
        return self.verses(99, 0)

    def verses(self, upper: int, lower: int) -> str:
        verse_numbers = reversed(list(range(lower, upper + 1)))
        return "\n".join(self.verse(number) for number in verse_numbers)
