import pytest

from bottles import Bottles

VERSE = {
    0: "No more bottles of beer on the wall, " + \
       "no more bottles of beer.\n" + \
       "Go to the store and buy some more, " + \
       "99 bottles of beer on the wall.\n",
    1: "1 bottle of beer on the wall, " + \
       "1 bottle of beer.\n" + \
       "Take it down and pass it around, " + \
       "no more bottles of beer on the wall.\n",
    2: "2 bottles of beer on the wall, " + \
       "2 bottles of beer.\n" + \
       "Take one down and pass it around, " + \
       "1 bottle of beer on the wall.\n",
    3: "3 bottles of beer on the wall, " + \
       "3 bottles of beer.\n" + \
       "Take one down and pass it around, " + \
       "2 bottles of beer on the wall.\n",
    4: "4 bottles of beer on the wall, " + \
       "4 bottles of beer.\n" + \
       "Take one down and pass it around, " + \
       "3 bottles of beer on the wall.\n",
    10: "10 bottles of beer on the wall, " + \
        "10 bottles of beer.\n" + \
        "Take one down and pass it around, " + \
        "9 bottles of beer on the wall.\n",
    99: "99 bottles of beer on the wall, " + \
        "99 bottles of beer.\n" + \
        "Take one down and pass it around, " + \
        "98 bottles of beer on the wall.\n",
}


@pytest.mark.parametrize(
    "number", [0, 1, 2, 3, 4, 10, 99],
)
def test_verse(bottles: Bottles, number: int) -> None:
    assert bottles.verse(number) == VERSE[number]


@pytest.mark.parametrize(
    "number", [-2, -1, 100],
)
def test_verse_index_error(bottles: Bottles, number: int) -> None:
    with pytest.raises(IndexError):
        bottles.verse(number)
