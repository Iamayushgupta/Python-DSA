#inserting element in its right position
#stable sort
# in place sort

def insertion_sort(a):
    for i in range(1,len(a)):
        temp=a[i]
        j=i-1

        while j>=0 and a[j]>temp:
            a[j+1]=a[j]
            j-=1
        a[j+1]=temp
    return a

list1=[6,3,1,5,9,8]
print(insertion_sort(list1))

