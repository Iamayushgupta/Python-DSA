#not in place sort
#stable sort

def merge(a1,a2,temp):
    i=0
    j=0
    k=0
    n1=len(a1)
    n2=len(a2)

    while i<=n1-1 and j<=n2-1:
        if a1[i]<a2[j]:
            temp[k]=a1[i]
            i+=1
        else:
            temp[k]=a2[j]
            j+=1
        k+=1

    while i <=n1-1:
        temp[k]=a1[i]
        i+=1
        k+=1

    while j <=n1-1:
        temp[k]=a1[j]
        j+=1
        k+=1

#a1 and a2 are two sorted list

#n1 and n2 are length of two list given sorted list
# temp=[None]*(n1+n2)




    