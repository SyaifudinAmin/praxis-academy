from modulsort import insertionSort,merge,timSort,printArray,sebelum,sesudah,randomangka

r = 32
j = randomangka()
k = len(j)

sebelum()
printArray(j,k)

timSort(j,k,r)

sesudah()
printArray(j,k)