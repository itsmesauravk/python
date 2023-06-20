#Lists are ordered, mutable, allow duplicate elements

myList = ["apple", "banana","car",'mango']
# print(myList)


#for checking
if "apple" in myList:
    print('avilable')
else:
    print('Out of stock')
# appending the items
myList.append("mancome")  #this will be added to last
myList.insert(1,"second") #this will be added to the first index  .index(index_num,item)
# print(myList)

#pop is used to remove last from list
item = myList.pop()
# print(item)
# print(myList)
# to remove specific
myList.remove("car")
# print(myList)
# to reverse the list 
myList.reverse()
# print(myList)
# to sort the list 
myList.sort()
# print(myList) #from a-z and 1 < 
#another type of sorting by making new item
item_new = sorted(myList)
# print(item_new)

list_1 = [0]*5 
# print(list_1)  this will print [0,0,0,0,0]

list_2 = ['a','b']
total_l = list_1 + list_2
# print(total_l) this will add both => [0,0,0,0,0,'a','b']

#slicing

list_A = [0,1,2,3,4,5]
a = list_A[1:4]
# print(a) this will slice the list and print [1,2,3] exclude the last given index 
b = list_A[::2]
# print(b) this will jump two steps and display the values [0,2,4] 
c = list_A[1::2]
# print(c) this will jump two steps starting from first index => [1,3,5]

#copying list
org_lst = [1,2,3]
cpy_lst = org_lst.copy() #.copy is used to create copy
cpy_lst.append(4)
# print(org_lst,cpy_lst)  so orglst prints =>[1,2,3] cpylst prints =>[1,2,3,4]

#list comprehension
mainList = [1,2,3]
check = [i*2 for i in mainList] #[(calculation) (for loop to iterate over mainlist)]
# print(check)  prints the result where every elements will multiplied by 2 =>[2,4,6]


