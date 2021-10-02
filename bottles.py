def successor(number: int) -> int:
    if number == 0:
        return 99
    else:
        return number - 1


class BottleNumber(object):
    def __init__(self, number: int):
        self.number = number

    @property
    def unit(self) -> str:
        if self.number == 0:
            return "no more"
        elif self.number == -1:
            return "99"
        else:
            return str(self.number)

    @property
    def successor(self) -> int:
        if self.number == 0:
            return 99
        else:
            return self.number - 1

    @property
    def container(self) -> str:
        if self.number == 1:
            return "bottle"
        else:
            return "bottles"

    @property
    def action(self) -> str:
        if self.number == 0:
            return "Go to the store and buy some more, "
        elif self.number == 1:
            return "Take it down and pass it around, "
        else:
            return "Take one down and pass it around, "


class Bottles(object):
    def verse(self, number: int) -> str:
        bottle_number = BottleNumber(number)
        successive_bottle_number = BottleNumber(successor(number))
        if number < 0 or number > 99:
            raise IndexError("The verse number N should be 0 <= N <= 99.")
        else:
            return f"{bottle_number.unit.capitalize()} {bottle_number.container} of beer on the wall, " + \
                   f"{bottle_number.unit} {bottle_number.container} of beer.\n" + \
                   f"{bottle_number.action}" + \
                   f"{successive_bottle_number.unit} {successive_bottle_number.container} of beer on the wall.\n"

    def song(self) -> str:
        return self.verses(99, 0)

    def verses(self, upper: int, lower: int) -> str:
        verse_numbers = reversed(list(range(lower, upper + 1)))
        return "\n".join(self.verse(number) for number in verse_numbers)
