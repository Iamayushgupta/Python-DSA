#improvement of insertion sort
# sorting with increments 5,3,1
#last increment must be 1 hence we take h as odd value
#unstable sort

#O(n(logn)**2)
#inplace sort

#elements can move a long distance

def shell_sort(a):
    h=int(input("Enter the maximum value (odd value)  :  "))
    while h>=1:
        for i in range(h,len(a)):
            temp=a[i]
            j=i-h
            while j>=0 and a[j]>temp:
                a[j+h] = a[j]
                j=j-h
            a[j+h]=temp
        h-=2
    return a

l1=[65,73,21,90,6,239,3,45,62,1,78,47,98,19,34]
print(shell_sort(l1))


# for insertion sort to work efficiently:
#     size of list must be small
#     list should be almost sorted

# Now if increment is large , size of sublist is small in shell sort

# now at the end, increment is one but it is efficient because list is almost sorted

#KNUTH algo

# h(1)=1 h(i+1)=3*h(i) + 1
