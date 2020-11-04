# Collections are containers that are used to store collections of data for example: list, dict, set, tuple etc
# -------------------------------------Counter-------------------------------------
# It is a container that stores elements as dict keys and their counts as dict values
import collections
from collections import Counter
a = "aaaaaaaccccccfffrrr"
my_counter = Counter(a)
print(my_counter) # Counter({'a': 7, 'c': 6, 'f': 3, 'r': 3})
print(my_counter.items()) # dict_items([('a', 7), ('c', 6), ('f', 3), ('r', 3)])
print(my_counter.keys()) # dict_keys(['a', 'c', 'f', 'r'])




