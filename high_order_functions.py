# #funtions filter
# my_lista = [1,2,4,5,7,8,9,6, 15,21,10]
# odd = list(filter(lambda x: x%2 != 0, my_lista))
#print(my_lista)
# print(odd)

# # funtions map
# my_lista = [1, 2, 4, 5, 7, 8, 9, 6, 15, 21, 10]
# squared = list(map(lambda x: x**2, my_lista))
# print(my_lista)
# print(squared)


# funtions reduce
from functools import reduce

my_lista = [2,2,2,2,2]
all_multiplied = reduce(lambda a, b: a*b, my_lista)
print(my_lista)
print(all_multiplied)
