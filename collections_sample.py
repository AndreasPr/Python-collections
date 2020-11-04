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
print(my_counter.values()) # dict_values([7, 6, 3, 3])
print(my_counter.most_common(1)) #[('a', 7)] the most common type
print(my_counter.most_common(2)) #[('a', 7), ('c', 6)] the 2 most common type
print(my_counter.most_common(1)[0]) #It gives us the tuple: ('a', 7)
print(my_counter.most_common(1)[0][0]) #It gives us the element of tuple with the most common type: a
print(list(my_counter.elements())) #['a', 'a', 'a', 'a', 'a', 'a', 'a', 'c', 'c', 'c', 'c', 'c', 'c', 'f', 'f', 'f', 'r', 'r', 'r']


# -------------------------------------Namedtuple-------------------------------------
from collections import namedtuple
# Lightweight object type

Point = namedtuple('Point', 'x,y')
pt = Point(1,-5)
print(pt) #Point(x=1, y=-5)
print(pt.x) # 1
print(pt.y) # -5

#--------------------------------------OrderedDict--------------------------------
from collections import OrderedDict
ordered_dict = OrderedDict()
ordered_dict['b'] = 2
ordered_dict['c'] = 3
ordered_dict['a'] = 1
print(ordered_dict) #OrderedDict([('b', 2), ('c', 3), ('a', 1)])

#---------------------------------------DefaultDict---------------------------------
from collections import defaultdict
d = defaultdict(int)
d['a'] = 1
d['b'] = 2
print(d['a']) # 1
print(d['c']) # 0. It does not exist, so returns the default value of int (which is the type of dict)

#------------------------------------------Deque------------------------
#Double ended queue and can be used to add and remove elements from both ends.
from collections import deque
d = deque()
d.append(1)
d.append(2)
print(d) #deque([1, 2])

d.appendleft(3)
print(d) #deque([3, 1, 2])

d.pop()
print(d) #deque([3, 1])

d.popleft()
print(d) #deque([1])

d.extend([4,5,6])
print(d) #deque([1, 4, 5, 6])

d.extendleft([1,9,0])
print(d) #deque([0, 9, 1, 1, 4, 5, 6])

d.rotate(1)
print(d) #deque([6, 0, 9, 1, 1, 4, 5])

d.rotate(-1)
print(d) #deque([0, 9, 1, 1, 4, 5, 6])