from math import sqrt
from rich import print

# Given a string, count total number of consonants in it
def count_consonants(my_str: str, count:int = 0) -> int:
	if my_str == "":
		return count
	else:
		if my_str[0] not in set(("a", "e", "i", "o", "u")):
			count = count + 1
		return count_consonants(my_str[1:], count)

# tests
assert count_consonants("blabaaaaax") == 4
assert count_consonants("xxxxx") == 5

# Given two number x and y find their product
def my_product(x:int, y: int, result:int =0) -> int:
	if y==0 or x==0:
		return result
	else:
		return my_product(x,y-1,result+x)

# tests
assert my_product(3,6) == 18

# Given a number n, check whether it’s prime number or not
def isprime(x:int, divisor:int=2)->bool:
	if divisor>=sqrt(x):
		return True
	else:
		if x%divisor == 0:
			return False
		else:
			return isprime(x, divisor + 1)

#tests
assert isprime(227) is True
assert isprime(23) is True
assert isprime(199) is True
assert isprime(4_507) is True
assert isprime(29_717) is True
assert isprime(16_763) is True
assert isprime(15_721) is False


# Given an integer K. Task is to print all binary strings of size K
def all_bin_str(k:int, working_res=None):
	if working_res is None:
		working_res = []
	if k==0:
		return working_res
	else:
		if working_res == []:
			results = ["0", "1"]
		else:
			results = []
			for item in working_res:
				results.append(item + "0")
				results.append(item + "1")
		return all_bin_str(k-1, results)


print(all_bin_str(3))
# tests
for n in range(1, 6):  # functions fails if passing 0 as length, also because the formula doesn't work
	assert len(all_bin_str(n)) == 2**n



print("[magenta]All tests successful √")
