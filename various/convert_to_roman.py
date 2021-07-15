import attr


@attr.s
class RomanNumber:
    """Takes one parameter, an integer between 1 and 999, and creates an object that has the attribute roman_num that is a string representing the original integer in roman number format. Example usage: print(RomanNumber(88))"""

    arabic_num = attr.ib()
    roman_num = attr.ib(init=False)

    @arabic_num.validator
    def _check_arabic_num(self, attribute, value):
        min_bound, max_bound = (1, 999)
        if value > max_bound or value < min_bound:
            raise ValueError(
                f"You passed the number {value} but this only works to convert numbers between {min_bound} and {max_bound}."
            )

    @roman_num.default
    def _roman_num_def(self):
        def _convert_single(elem: int, unit: str, half: str, upper: str):
            if elem == 1:
                return unit
            if elem == 2:
                return unit * 2
            if elem == 3:
                return unit * 3
            if elem == 4:
                return unit + half
            if elem == 5:
                return half
            if elem == 6:
                return half + unit
            if elem == 7:
                return half + unit * 2
            if elem == 8:
                return half + unit * 3
            if elem == 9:
                return unit + upper
            if elem == 0:
                return ""

        list_repres = [int(x) for x in str(self.arabic_num)]
        str_repres = ""

        for i, el in enumerate(list_repres[::-1]):
            if i == 0:
                str_repres = _convert_single(el, "i", "v", "x") + str_repres
            if i == 1:
                str_repres = _convert_single(el, "x", "l", "c") + str_repres
            if i == 2:
                str_repres = _convert_single(el, "c", "d", "m") + str_repres

        return str_repres.upper()


for i in range(100, 1001, 100):
    print(i, RomanNumber(i))
