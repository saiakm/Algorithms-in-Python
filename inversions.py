#Counting inversions
def merge_and_count(B,C,n1,n2):
    count= 0
    A,i,j = [],0,0
    while i<n1 or j<n2:
        if j>=n2 or (i<n1 and B[i]<=C[j]):
            A.append(B[i])
            i+=1
            count+=j
        else:
            A.append(C[j])
            j+=1
    return (A,count)

def sort_and_count(A,n):
    if n<=1:
        return (A,0)
    else:
        (B,m1) = sort_and_count(A[:n//2],n//2)
        (C,m2) = sort_and_count(A[n//2:],n-n//2)
        (A,m3) = merge_and_count(B,C,n//2,n-n//2)
        return (A,m1+m2+m3)
#A=[3,8,12,20,32,48,5,7,9,25,29]
#n = len(A)
#print(sort_and_count(A,n))

input_array=[]
try:
    while 1:
        input_line = input()
        if input_line == "":
            break
        input_array.append(input_line)
except EOFError as e:
    pass

n = input_array[0]
n = int(n)
A = []
for i in range(1,n+1):
    A.append(int(input_array[i]))
#print(A)
print(sort_and_count(A,n)[1])

