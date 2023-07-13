#deleteing the last node of heap and storing the max value in new arr
#worst case and best complexity is O(nlogn)
#not a stable sort
# in place sort( space complexity === O(1))

def heap_sort(a,n):
    build_heap_bottom_up(a,n)
    while n>1:
        maxvalue=a[1]
        a[1]=a[n]
        a[n]=maxvalue
        n-=1
        restore_down(1,a,n)
    return a

def build_heap_bottom_up(a,n):
    i=n//2
    while i>=1:
        restore_down(i,a,n)
        i-=1
def restore_down(i,a,n):
    k=a[i]
    lchild=2*i
    rchild=lchild + 1

    while rchild<=n:
        if k>=a[lchild] and k>=a[rchild]:
            a[i]=k
            return
        elif a[lchild]>a[rchild]:
            a[i]=a[lchild]
            i=lchild
        else:
            a[i]=a[rchild]
            i=rchild
        
        lchild=2*i
        rchild=lchild+1

    if lchild==n and k<a[lchild]:
        a[i]=a[lchild]
        i=lchild
    a[i]=k

n=int(input("Enter the number of elemnets : "))
a=[None]*(n+1)
for i in range(1,n+1):
    a[i]=int(input("Enter the element  :  "))

print(heap_sort(a,n))


