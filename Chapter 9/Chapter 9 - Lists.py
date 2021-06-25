a = []
print(type(a))

myList = [1, 2, 3,4,5]

print(myList[0])
print(myList[4])
print(len(myList))

print(myList[1:3])
print(myList[:3])
print(myList[1:])

newList = ['dog', 2, 10.5, True, 'a']
print(newList)
print(newList[0])

newList[1] = 'cat'
print(newList)
newList.append(5)
print(newList)

newList.insert(2, 'elephant')
print(newList)

# for i in newList:
#     if i == 'cat':
#         print("Cat found")

if 'cat' in newList:
    print("Cat is in newList")

if 'lion' in newList:
    print("Lion is in newList")

for x in newList:
    print(x)

newList.remove("cat")
print(newList)

newList.pop(1)
print(newList)

newList.pop()
print(newList)

list1 = newList
print(list1)
#newList.pop()
#print(list1)

list1 = newList.copy()
newList.pop()
print("List1",list1)
print("newList", newList)

oddNumRange = range(1, 10, 2)
print(oddNumRange)
num = list(oddNumRange)
print(num)

sum_of_num = 0
for j in num:
    sum_of_num += j

print(sum_of_num)

print(sum(num))
print(max(num))
print(min(num))
print(sum(num)/len(num))


mList = [[1,2,3],
         [4,5,6],
         [7,8,9],
         [10,11,12]]
print(mList)

print(mList[0])
print(mList[0][1])
print(mList[2][2])

print(mList[0:2])
mList.append([13,14,15])
print(mList)

for x in mList:
    for y in x:
        print(y)

        





