#list Examples

numbers = [10,20,30,40]

#tuple examples

coordinates = (5,10)

print(numbers)
print(coordinates)

#indexing
#2 types - positive and negative
#positive -> 0,1,2,3,4,.....left to right
#negative -> -1,-2,-3,-4,...right ti left

list = [100,200,300,500,600,700,800,900,1000]
#range indexing
#negative index can't be done in reverse order...
print(list[-3:-1])

#steps or skips start_index:end_index:skip
print(list[1:4:1])
print(list[1:4:2])
print(list[1:4:3])
print(list[2:9:2])
print(list[2:9:3])
print(list[-8:-1])

#append,insert,extend,pop,sort,delete,clear
list.sort(reverse=True)
print(list)
print(list[::-1])

