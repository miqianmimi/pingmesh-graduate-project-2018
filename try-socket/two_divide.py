def two_divide_find(A,start,end,num):
    if A[-1]<num or A[0]>num:
        return("找不到")
    if start==end:
        if num == A[start-1]:
            return start
        else:
            return("找不到")
    m = int((start + end) / 2) -1
    if num<A[m]:
        return two_divide_find(A,start,m-1,num)
    if num>A[m]:
        return two_divide_find(A,m+1,end,num)
    if num==A[m]:
        return int((start+end)/2)
#a=two_divide_find([1,2,3,4,5,6,67,75,75,100],1,10,100)
a=two_divide_find([1,3,4,5],1,2,0)

print(a)

#写好了~~~~~~

