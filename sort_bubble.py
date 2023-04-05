#swapping between adjacent elements
# after every pass we get nth largest element 

# data sensitive order
# O(n**2)

def bubble_sort(a):
    for i in range(len(a)-1,0,-1):
        for j in range(i):
            if a[j] > a[j+1]:
                a[j],a[j+1] = a[j+1] , a[j]
    return a

list1=[6,3,1,5,9,8]
print(bubble_sort(list1))

#improvement in bubble sort

#we count number of swaps
# if swaps==0 it means array has become sorted

def bubble_sort_imp(a):
    for i in range(len(a)-1,0,-1):
        swaps=0
        for j in range(i):
            if a[j] > a[j+1]:
                swaps+=1
                a[j],a[j+1] = a[j+1] , a[j]
        if swaps==0:
            break
    return a