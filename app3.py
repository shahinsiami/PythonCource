from ast import ListComp
from audioop import reverse
from enum import unique
from traceback import print_tb


letters = ["a","b","c"]
matrix = [[0,1],[2,3]]
zeros = [0] * 5
combined = zeros + letters
numbers = list(range(20))
chars= list("hello world")
print(letters)
print(matrix)
print(zeros)
print(combined)
print(numbers)
print(chars)
##################
list_count = ["a","b","c","d","e"]
list_count[0] = "A"
print(list_count[0:4:2])
print(list_count[::2])
list_range = list(range(20))
print(list_range[::-1])
################## 
list_unpack = [0,1,2,3,4,5,5,5,5]
first,second,third,*other = list_unpack
print(first)
print(second)
print(other)
################## 
loop_list = ["a","b","c"]
for index , loop_list in enumerate(loop_list):
    print(index,loop_list)

##################
add_remove_list = ["a","b","c","d"]
add_remove_list.append("e")
print(add_remove_list)
add_remove_list.insert(0,"e")
print(add_remove_list)
add_remove_list.insert(0,"e")
print(add_remove_list)
add_remove_list.pop(0)
print(add_remove_list)
add_remove_list.remove("a")
print(add_remove_list)
del add_remove_list[0:3]
print(add_remove_list)
add_remove_list.clear()
print(add_remove_list)
##################
list_finding = ["a","b","c","d"]
print(list_finding.index("a")) #if not exist error
print(list_finding.count("e"))
if "e" in list_finding:
    print(list_finding.index("e"))
##################    
number_sort = [1,2,3,4,5,6,7,8]
number_sort.sort()
print(number_sort)
number_sort.sort(reverse=True)
print(number_sort)
print(sorted(number_sort))
print(number_sort)
print(sorted(number_sort,reverse=True))
##################
item_sort = [
    ("product1",1305),
    ("product1",120),
    ("product1",10),
]
def sort_item(item_sort):
    return item_sort[1]
item_sort.sort(key=sort_item)
print(item_sort)
##################
item_sort = [
    ("product1",1305),
    ("product1",120),
    ("product1",10),
]
item_sort.sort(key=lambda item_sort:item_sort[1])
print(item_sort)
##################
item_sort_map = [
    ("product1",1305),
    ("product1",120),
    ("product1",10),
]
prices = []
for item in item_sort_map:
    prices.append(item[1])

print(prices)
map_list = list(map(lambda item:item[1],item_sort_map))
print(map_list)
##################
item_compression = [
    ("product1",13015),
    ("product1",1250),
    ("product1",150),
]
##[expression for item in items]
price_compression = [item[1] for item in item_compression]
print(price_compression)
##################
list_combine1 = [1,2,3]
list_combine2 = [10,20,30]
print(list(zip(list_combine1,list_combine2)))
print(list(zip("abc",list_combine1,list_combine2)))
##################
#lifo last in - first out = stack
browsing_session = []
browsing_session.append(1)
browsing_session.append(2)
browsing_session.append(3)
print(browsing_session)
last = browsing_session.pop()
print(last)
print(browsing_session)
##################
#fifo first in first out Queues
from collections import deque
queue = deque([])
queue.append(1)
queue.append(2)
queue.append(3)
queue.append(4)
queue.popleft()
print(queue)
if not queue:
    print("empty")
##################
#tuple cant modify object
point = (1,2)
point_with_out_mark = 1,2
point_with_out_inteeger = 1
empty_tuple = ()
print(type(point),type(point_with_out_mark),type(point_with_out_inteeger,))
sum_point = (1,2) + (3,4)
print(sum_point)
multy_point = (1,2) * 2
print(multy_point)
conver_tuple = tuple("hi world")
print(conver_tuple)
tuple_point = (1,2,3)
print(tuple_point[0:2])
##################
from array import array
numbers_array = array ("i",[1,2,3])
numbers_array[0] = 1
print(numbers_array)
##################
number_set = [1,2,3,4,5,5]
uniques = set(number_set)
print(uniques)
first = uniques
second = {1,4,6}
print(first | second)
print(first & second)
print(first - second)
print(first ^ second)
##################
#dictionary
dictionary = {"x":1,"y":2}
dictionary_dic = dict(x=1,y=2)
print(dictionary,dictionary_dic)
##################
from sys import getsizeof
values = (x * 2 for x in range (100000))
print(getsizeof(values))
values = [x * 2 for x in range (100000)]
print(getsizeof(values))
##################
first = {"x":1}
second = {"x":10,"y":20}
combined = {**first , **second,"z":1}
print(combined)
##################
