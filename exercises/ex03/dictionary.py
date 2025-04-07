"""this is an assignment based on dictionaries"""

__author__: str = "730578258"

# note: include 2 use case (describing an expected scenario)
# note: include 1 edge case (unexpected scenario)


def invert(input_dict: dict[str, str]) -> dict[str, str]:
    """Should invert the keys and values in the dictionary"""
    inverted_dict: dict[str, str] = {}

    for key in input_dict:
        value: str = input_dict[key]
        if value in inverted_dict:
            raise KeyError("there is a duplicate!")
        inverted_dict[value] = key
    return inverted_dict


def count(input_val: list[str]) -> dict[str, int]:
    """count the frequency of occurrences in the list"""
    results: dict[str, int] = {}
    for item in input_val:
        if item in results:  # if the value is already found in the dictionary
            results[item] += 1  # increase its count
        else:  # if value is not found in dictionary already
            results[item] = 1  # keep count as 1
    return results


def favorite_color(color_dict: dict[str, str]) -> str:
    """determines the most frequently occurring color in the input"""
    colors_list = []  # creates a list of colors
    for color_name in color_dict:
        colors_list.append(color_dict[color_name])  # shoudl extract each color value

    colors_counts = count(colors_list)
    # to find the most common color hopefully
    max_color = ""
    max_color_count = 0
    for color in colors_list:
        if colors_counts[color] > max_color_count:
            max_color = color
            max_color_count = colors_counts[color]
    return max_color


def bin_len(words: list[str]) -> dict[int, set[str]]:
    """bins a list of words by their length to store in sets"""
    category = {}
    for word in words:
        length = len(word)
        if length not in category:
            category[length] = set()
        category[length].add(word)
    return category
