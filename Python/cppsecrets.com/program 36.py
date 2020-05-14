"""Python Program to Compute Prime Factors of an Integer"""

import re

num = int(input())

factors = [n for n in range(1,num + 1) if num % n == 0]

#primefact = re.compile(r'^1?$|^(11+)\1+$').match('1' * factors) is None

prime_nums = [x for x in range(2, factors) if all(x % k for k in range(2, x-1))]


print(factors)
print(prime_nums)

#print([x for x in range(primefact)])