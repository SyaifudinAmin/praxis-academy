import random
#Text---------------------------------------------
def sebelum ():
    print ("Data Sebelum diurutkan :")

def sesudahquick ():
    print ("Data Sesudah diurutkan dengan quick sort:")
def sesudahselect ():
    print ("Data Sesudah diurutkan dengan selection sort:")
def sesudahtim ():
    print ("Data Sesudah diurutkan dengan tim sort:")
def sesudahbubble ():
    print ("Data Sesudah diurutkan dengan bubble sort:")
def sesudahinsert ():
    print ("Data Sesudah diurutkan dengan insertion sort:")
#Ranfdom Angka-----------------------------------------------
def randomangka():
    angka = []
    angka = [random.randint(0,100) for n in range(10)]
    return angka
    # print (angka)
#Quick Sort --------------------------------------
def quickSort(alist):

  quickSortHelper(alist,0,len(alist)-1)

def quickSortHelper(alist,first,last):

  if first<last:
      splitpoint = partition(alist,first,last)
      quickSortHelper(alist,first,splitpoint-1)
      quickSortHelper(alist,splitpoint+1,last)

def partition(alist,first,last):

  pivotvalue = alist[first]
  leftmark = first+1
  rightmark = last
  done = False

  while not done:
      while leftmark <= rightmark and alist[leftmark] <= pivotvalue:
          leftmark = leftmark + 1

      while alist[rightmark] >= pivotvalue and rightmark >= leftmark:
          rightmark = rightmark -1

      if rightmark < leftmark:
          done = True
      else:
          temp = alist[leftmark]
          alist[leftmark] = alist[rightmark]
          alist[rightmark] = temp

  temp = alist[first]
  alist[first] = alist[rightmark]
  alist[rightmark] = temp

  return rightmark

#Insertion Sort------------------------------------------------
def insertion(arr): 
  
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

#Bubble Sort ------------------------------
def functionbubble(llist):
    for number in range(len(llist)-1,0,-1):
        # print (number)
        for i in range(number):
            # print (i)
            if llist[i]>llist[i+1]:
                temp = llist[i]
                llist[i] = llist[i+1]
                llist[i+1] = temp

#Selection Sort-----------------------------------------------
def functionselection(llist): 
    for i in range(len(llist)): 
        
        #mencari elemen terkecil
        min_idx = i 
        for j in range(i+1, len(llist)): 
            if llist[min_idx] > llist[j]: 
                min_idx = j 
                
        #menukar elemen terkecil dengan elemen pertama         
        llist[i], llist[min_idx] = llist[min_idx], llist[i]

#Tim Sort -------------------------------------------------------
#mengurutkan indeks dari kiri ke kanan dengan ukuran yang paling besar pada RUN
def insertionSort(arr, left, right): 

	for i in range(left + 1, right+1): 
	
		temp = arr[i] 
		j = i - 1
		while arr[j] > temp and j >= left: 
		
			arr[j+1] = arr[j] 
			j -= 1
		
		arr[j+1] = temp 
	
# menggabungkan nilai yang sudah di urutkan run 
def merge(arr, l, m, r): 

	#memisah array dalam 2 bagian
	len1, len2 = m - l + 1, r - m 
	left, right = [], [] 
	for i in range(0, len1): 
		left.append(arr[l + i]) 
	for i in range(0, len2): 
		right.append(arr[m + 1 + i]) 
	
	i, j, k = 0, 0, l 
	# setelah membandingkan , kemudian di gabungkan dalam sub array
	while i < len1 and j < len2: 
	
		if left[i] <= right[j]: 
			arr[k] = left[i] 
			i += 1
		
		else: 
			arr[k] = right[j] 
			j += 1
		
		k += 1
	
	# menyalin elemen yang ada di kiri jika masih tersisa 
	while i < len1: 
	
		arr[k] = left[i] 
		k += 1
		i += 1
	
	# menyalin elemen yang ada di kanan jika masih tersisa
	while j < len2: 
		arr[k] = right[j] 
		k += 1
		j += 1
	
# mengurutkan array[0...n-1] mirip merge sort
def timSort(arr, n, RUN): 
    # RUN = 32
	# sorting sub array dengan run
	for i in range(0, n, RUN): 
		insertionSort(arr, i, min((i+31), (n-1))) 
	
	# mulai menggabungkan dari ukuran run (32).
	# akan digabungkan ke ukuran 64, kemudian 128, 256, dst
	size = RUN 
	while size < n: 
	
		# mengambil nilai awal dari array kiri.
		# menggabungkan  arr[left..left+size-1] dan arr[left+size, left+2*size-1]
		# setelah semua di gabungkan, ukuran left di jadikan 2*size
		for left in range(0, n, 2*size): 
		
			# find ending point of left sub array 
			# mid+1 is starting point of right sub array 
			mid = left + size - 1
			right = min((left + 2*size - 1), (n-1)) 
	
			# merge sub array arr[left.....mid] & 
			# arr[mid+1....right] 
			merge(arr, left, mid, right) 
		
		size = 2*size 
		
# utility function to print the Array 
def printArray(arr, n): 

	for i in range(0, n): 
		print(arr[i], end = " ") 
	print() 