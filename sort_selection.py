# find smallest element and then swap
#O(n**2)
#unstable sort

def selection_sort(a):
    for i in range(len(a)-1):
        minindex = i
        for j in range(i+1,len(a)):
            if a[j] < a[minindex]:
                minindex=j
        if i!=minindex:
            a[i],a[minindex] = a[minindex] , a[i]

    return a

list1=[6,3,1,5,9,8]
print(selection_sort(list1))
