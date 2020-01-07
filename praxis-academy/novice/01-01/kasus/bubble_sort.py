def functionbubble(llist):
    for number in range(len(llist)-1,0,-1):
        # print (number)
        for i in range(number):
            # print (i)
            if llist[i]>llist[i+1]:
                temp = llist[i]
                llist[i] = llist[i+1]
                llist[i+1] = temp

m = [14, 23, 12, 42, 37, 3, 34, 22, 1, 19]
functionbubble(m)
print(m)


#print (range (len(m)-1,0,2))
#range (start,stop,step)
#star : tidak bisa di ++
#stop :sebagai batas khir dri range /= < dari range
