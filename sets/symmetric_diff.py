a = input()
lis = a.split()
newlist = list(map(int, lis))
setA = set(newlist)

a = input()
lis = a.split()
newlist = list(map(int, lis))
setB = set(newlist)

list_result = list(setA.symmetric_difference(setB))
list_result.sort()

for i in range(len(list_result)):
    print(list_result[i])
