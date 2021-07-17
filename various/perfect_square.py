import math

from rich import print


def is_square(num: int) -> bool:
    """Takes an int, returns if it's a perfect square."""
    my_sqrt = math.sqrt(num)
    if int(my_sqrt) != my_sqrt:
        return False
    else:
        return True


a = int(input("Please enter an integer: "))  # throws exception if not int
if not is_square(a):
    cond = "[magenta]is not[/]"
else:
    cond = "[green]is[/]"
print(f"{a} {cond} a [yellow]perfect square[/].")
