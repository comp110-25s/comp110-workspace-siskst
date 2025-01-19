""" 
The goal of this program is to plan a tea party by 
calculating the number of tea bags, treats and overall costs
based on the number of guests at the party.
"""

__author__: str = "730578258"


def main_planner(guests: int) -> None:
    """
    this function organizes the tea party planning and prints the results
    after calling the functions below.
    """

    tea_count = tea_bags(guests)
    treat_count = treats(guests)
    total_cost = cost(tea_count, treat_count)

    print(f"A Cozy Tea party for {guests} People!")
    print(f"Tea Bags: {tea_count}")
    print(f"Treats: {treat_count}")
    print(f"Cost: ${total_cost}")

    return None


def tea_bags(people: int) -> int:
    """
    Calculates the number of tea bags needed for the party since
    each guest drinks 2 cups of tea.
    """
    return people * 2


def treats(people: int) -> int:
    """
    Calculates the number of treats needed.
    Assumes each guest eats 1.5 treats per tea drank by guests.
    """
    return int(tea_bags(people=people) * 1.5)


def cost(tea_count: int, treat_count: int) -> float:
    """
    Cost function returns the total cost of tea and treats combined,
    if the tea bag is $0.50 and each treat is $0.75.
    """
    return 0.50 * tea_count + 0.75 * treat_count


if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party? ")))
