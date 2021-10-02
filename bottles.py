def unit(number: int) -> str:
    if number == 0:
        return "no more"
    elif number == -1:
        return "99"
    else:
        return str(number)


def successor(number: int) -> int:
    if number == 0:
        return 99
    else:
        return number - 1


def container(number: int) -> str:
    if number == 1:
        return "bottle"
    else:
        return "bottles"


def action(number: int) -> str:
    if number == 0:
        return "Go to the store and buy some more, "
    elif number == 1:
        return "Take it down and pass it around, "
    else:
        return "Take one down and pass it around, "


class Bottles(object):
    def __init__(self):
        pass

    def verse(self, number: int) -> str:
        if number < 0 or number > 99:
            raise IndexError("The verse number N should be 0 <= N <= 99.")
        else:
            return f"{unit(number).capitalize()} {container(number)} of beer on the wall, " + \
                   f"{unit(number)} {container(number)} of beer.\n" + \
                   f"{action(number)}" + \
                   f"{unit(successor(number))} {container(successor(number))} of beer on the wall.\n"

    def song(self) -> str:
        return self.verses(99, 0)

    def verses(self, upper: int, lower: int) -> str:
        verse_numbers = reversed(list(range(lower, upper + 1)))
        return "\n".join(self.verse(number) for number in verse_numbers)
