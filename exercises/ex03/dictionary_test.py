"""this file tests the values in the dictionary"""

__author__: str = "730578258"


import pytest
from exercises.ex03.dictionary import invert, favorite_color, count, bin_len


# testing the invert function (2 use and 1 edge )


def test_invert_standard_single():  # use case
    """Testing to see if it inverts lists normally"""
    assert invert({"cup": "glass"}) == {"glass": "cup"}


def test_invert_standard():  # 2nd use case
    """2nd use case testing if this can invert an actual list"""
    assert invert(
        {"small": "frenchie", "big": "mastiff", "medium": "staffie", "teacup": "poodle"}
    ) == {
        "frenchie": "small",
        "mastiff": "big",
        "staffie": "medium",
        "poodle": "teacup",
    }


def test_invert_empty():  # edge case to invert an empty dictionary
    """Edge case that inverts an empty dictionary."""
    assert invert({}) == {}


def test_invert_raises_keyerror() -> None:
    """Check if KeyError is raised when duplicate values exist."""
    with pytest.raises(KeyError):
        my_dictionary = {"kris": "jordan", "michael": "jordan"}
        invert(my_dictionary)  # This should raise a KeyError


# testing count


def test_count_empty():  # edge case
    assert count([]) == {}
    """Edge case: count occurrences in an empty list"""


def test_count_one_item():  # use case hopefully
    assert count(["apple"]) == {"apple": 1}


def test_count_multiple_items():
    assert count(
        ["brie", "cheddar", "swiss", "swiss", "swiss", "cheddar", "swiss"]
    ) == {"brie": 1, "cheddar": 2, "swiss": 4}


# testing favorite color
def test_single_favorite_color():  # use case
    """tests a case where one color is the noticeable favorite"""
    colors_dict = {"a": "green", "b": "green", "c": "blue", "d": "pink"}
    assert favorite_color(colors_dict) == "green"


def test_favorite_color_tie():  # use case
    """Use case for a tie between multiple colors"""
    assert (
        favorite_color(
            {
                "Frosty": "orange",
                "Rudolph": "orange",
                "Jack": "purple",
                "Klaus": "purple",
            }
        )
        == "orange"
    )


def test_favorite_color_same():  # ideally an edge case
    """edge case for when everyone has the same favorite color"""
    assert favorite_color({"Jim": "red", "Jam": "red", "Jon": "red"}) == "red"


# testing bin_len


def test_bin_len_empty():  # edge
    """Edge Case"""
    assert bin_len([]) == {}


def test_bin_len_single_word():  # use
    """Use Case 1: Bin a list with one word."""
    assert bin_len(["nuggets"]) == {7: {"nuggets"}}


def test_bin_len_multiple_():  # use
    """Bin words of varying lengths."""
    assert bin_len(["pot", "pan", "crockpot", "spork", "spoon"]) == {
        3: {"pot", "pan"},
        5: {"spork", "spoon"},
        8: {"crockpot"},
    }
