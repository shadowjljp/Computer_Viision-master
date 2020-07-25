import numpy as np
friend=["Kevin","Allen","Jim","Jim","Zelle",'Bill']
re =friend.pop()
print(friend)
print(re)
lucky_number=[4,8,3,1,0]
friend.extend(lucky_number)

print(friend)
#insert Kelly
friend.insert(1,'Kelly')
print("insert Kelly",friend)

#remove Kelly
friend.remove('Kelly')
print("#remove Kelly",friend)

#remove the last element
friend.pop()
print("remove the last element:", friend)

#get the index of certain element
print("Index of Zelle is ",friend.index("Zelle"))

#count the amount of certain elements of list
print("Jim has show up",friend.count("Jim"),"times in the list")

#sort the list
print("Sort list in ascending: ",lucky_number.sort())

#reverse the list
print("list has been reverse: ",lucky_number.reverse())

#copy list and become independent object
friend2 = friend.copy()
friend2.insert(1,"Tester")

print("Copy and modify list ",friend2)
print("original list: ",friend)
#clear List
friend.clear()
print("List has been clear ",friend)

#2D list
number = [[1,2,3],[4,5,6],[7,8,9]]
for x in number:
    for y in x:
        print("number ",y)
#3D list
n=3
#distance= [[[0 for k in range(n)] for j in range(n)] for i in range(n)]
distance=[[[0, 1, 2], [3, 0, 0], [6, 0, 0]],
          [[9, 0, 0], [12, 0, 0], [15, 0, 0]],
          [[18, 0, 0], [21, 0, 0], [24, 0, 0]]]
print("distance is : ",distance)
#print("distance[:,:,0] :",distance[:,:,0])  #Can not be accessing multi-dimension slicing
                                        #Solution: use nump array
distance=np.array(distance)
print("distance[:,:,0] :",distance[1:,1:,0])
