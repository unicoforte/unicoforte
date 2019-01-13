squares = [value**2 for value in range(1, 11)]

print(squares)

to_twenty = [print(value) for value in range(1, 21)]

# prints every number from 1 to 1 million
to_million = [print(number) for number in range(1, 1000001)]

to_million2 = list(range(1, 1000001))

# prints min, max, and sum for range of 1 to 1 million
print(min(to_million2))
print(max(to_million2))
print(sum(to_million2))

# prints odd numbers from 1 to 20
odds_to_twenty = [print(value) for value in range(1, 21, 2)]
