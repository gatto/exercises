from rich import print


def is_power_2(num: int) -> bool:
    """
    Takes an int (works with float too), returns if it's power of two.
    Try: 1427247692705959881058285969449495136382746624, two to the 150
    """
    # print(num)  # fun
    if num == 2:
        return True
    how_about = num / 2
    if int(how_about) != how_about:
        return False
    return is_power_2(int(how_about))


a = int(input("Please enter an integer: "))  # throws exception if not int
if not is_power_2(a):
    cond = "[magenta]is not[/]"
else:
    cond = "[green]is[/]"
print(f"{a} {cond} a power of [yellow]2[/].")
