set1 = {42, 'Monty Python', ('a', 'b', 'c')}
set2 = set1
set1.add(range(5, 10))
print(set2)

# {42, 'Monty Python', ('a', 'b', 'c'), range(5,10)}
# The variable set1 and set2 reference the same object and therefore any mutations 
# will be visible for both variables. 