# def functiinsertion(llist):
#     for index in range(1, len(llist)):
#         current = llist[index]
#         position = index

#         while position > 0 and llist[position-1] > current:
#             print("Swapped {} for {}".format(llist[position], llist[position-1]))
#             llist[position] = llist[position-1]
#             print(llist)
#             position -= 1

#         llist[position] = current

def insertionSort(arr): 
  
    # Traverse through 1 to len(arr) 
    for i in range(1, len(arr)): 
  
        key = arr[i] 
  
        # Move elements of arr[0..i-1], that are 
        # greater than key, to one position ahead 
        # of their current position 
        j = i-1
        while j >=0 and key < arr[j] : 
                arr[j+1] = arr[j] 
                j -= 1
        arr[j+1] = key 

m = [11, 21, 12, 42, 37, 3, 34, 22, 1, 19]
print ("Data Awal")
print(m)
insertionSort(m)
print("Hasil setelah  Sorting")
print (m)

# function insertionSortR(array A, int n)
#      if n > 0
#         insertionSortR(A, n-1)
#         x ← A[n]
#         j ← n-1
#         while j >= 0 and A[j] > x
#             A[j+1] ← A[j]
#             j ← j-1
#         end while
#         A[j+1] ← x
#      end if
#  end function

# for i in range(1, len(m)):
#     # print (i)
#     #i = 1 - 7;
#     key = m[i]
#     #print (key)
#     #key = n[i] = 2-8
#     j = i-1
#     # print ("ini j:", j)
#     while j >= 0 and key < m[j]:
#         # print (j)
#         m[j+1] = m[j]
#         j = j-1
#     m[j+1] = key
#     # print (key)
# print ('InsertionSort :')
# for i in range( len(m)):
#     print("% d" % m[i])

# def insertionSort(my_list):
    # for every element in our array