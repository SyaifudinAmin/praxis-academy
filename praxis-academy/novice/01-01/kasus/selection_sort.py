def functionselection(llist): 
    for i in range(len(llist)): 
        
        #mencari elemen terkecil
        min_idx = i 
        for j in range(i+1, len(llist)): 
            if llist[min_idx] > llist[j]: 
                min_idx = j 
                
        #menukar elemen terkecil dengan elemen pertama         
        llist[i], llist[min_idx] = llist[min_idx], llist[i]
         
m = [11, 21, 12, 42, 37, 3, 34, 22, 1, 19]  
functionselection(m) 
print ("Sorted array") 
print (m)
# for i in range(len(m)): 
#     print("%d "%m[i])