# Just needed for constant math.pi in the example below
import math

my_fruit_set = { "apple", "banana", "cherry", "apple", "plum", "mango", "avocado" }
my_stuff_set = { 20, "OAMK", "mango", 1.234, "avocado", math.pi }

# unsorted, also duplicate items are removed automatically                
print('my_fruit_set:', my_fruit_set)

# intersection of two sets
print('intersection:', my_fruit_set.intersection(my_stuff_set))
print('union:', my_fruit_set.union(my_stuff_set))

# empty set in python vs dictionary
empty_set = set()
print('empty_set', type(empty_set))
empty_dict = { } 
print('empty_dict', type(empty_dict))

empty_set.update(my_fruit_set)
print('empty_set update', empty_set)
empty_set.difference_update(my_stuff_set)
print('empty_set difference update:', empty_set)

empty_set = set(map(lambda x: x[1:], empty_set))
print('empty_set after map', empty_set)