m = [14, 23, 12, 42, 37, 3, 34, 22, 1, 19]

#print (range (len(m)-1,0,2))
#range (start,stop,step)
#star : tidak bisa di ++
#stop :sebagai batas khir dri range /= < dari range
# def bubbleSort(nlist):
for number in range(len(m)-1,0,-1):
    # print (number)
    for i in range(number):
        # print (i)
        if m[i]>m[i+1]:
            temp = m[i]
            m[i] = m[i+1]
            m[i+1] = temp
print(m)
