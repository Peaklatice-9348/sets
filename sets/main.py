#creating sets
my_set = {1,2,3,4,5}
print (my_set)

#converting a list to a set
list_1 = [1,2,2,3,3,3,4,1,2,3,3,2,1,3,4,3,3]
unique_numbers = set(list_1)
print (unique_numbers)

#iterating through a set
for i in my_set:
    print(i)

#modifying a set
#adding element
my_set.add(6)
print (my_set)

#removing elements
my_set.remove(6)
print (my_set)

#checking for element
print (10 in my_set)

#unique numbers that are not 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20
set_1 = {70983975,355454814,1234567898763,1000000000000000000000000000000000000,204320809701}
set_2 = {6519654,8543925485764262639,999999999999999999999999999999999,657894302,657876357653848765437654387654387654376542765}
new_set = set_1.union(set_2)
print (new_set)