def merge_sort(a):
    n=len(a)
    temp=[None]*n
    sort(a,temp,0,n-1)

    return a

def merge(a,temp,low1,up1,low2,up2):
    i=low1
    j=low2
    k=low1

    while i<=up1 and j<=up2:
        if a[i]<a[j]:
            temp[k]=a[i]
            i+=1
        else:
            temp[k]=a[j]
            j+=1
        k+=1
    while i <=up1:
        temp[k]=a[i]
        i+=1
        k+=1

    while j <=up2:
        temp[k]=a[j]
        j+=1
        k+=1

def copy(a,temp,low,up):
    for i in range(low,up+1):
        a[i]=temp[i]

def sort(a,temp,low,up):
    if low==up:
        return 

    mid=(low + up)//2
    sort(a,temp,low,mid)
    sort(a,temp,mid+1,up)

    merge(a,temp,low,mid,mid+1,up)
    copy(a,temp,low,up)

l1=[6,3,1,2,4]
print(merge_sort(l1))

