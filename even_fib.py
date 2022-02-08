'''
Name: Sebastian Vega
Description:
    calculate the sum of the even valued terms in the fibonacci sequence that do not exceed 4 million
'''

current = 2 # second term in fibonnaci sequence(current term)
past = 1 # first term in fibonacci sequence
evens = 0 # keeps sum of even terms

while current < 4000000: # loops until 4 million
    if current % 2 == 0: # checks if term is even
        evens += current # adds term to sum of evens

    current, past = past + current, current # creates fibonacci sequence

print(evens)

