
RUN = 32	
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
def timSort(arr, n): 

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

	

arr = [14, 23, 12, 42, 37, 3, 34, 22, 1, 19] 
n = len(arr) 
print("Data awal:") 
printArray(arr, n) 

timSort(arr, n) 

print("Data setelah diurutkan:") 
printArray(arr, n) 
