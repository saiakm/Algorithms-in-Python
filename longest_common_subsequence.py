#Longest Common Subsequence
def lcs(A,B):
    n = len(A)
    m = len(B)
    opt = []
    pi = []
    for i in range(0, n + 1):
        opt.append([])
        pi.append([])
        for j in range(0, m + 1):
            opt[i].append(0)
            pi[i].append("")
    #print(opt)
    #print(pi)


    for i in range(n):
        for j in range(m):
            if A[i]==B[j]:
                opt[i+1][j+1] = opt[i][j] + 1
                pi[i+1][j+1] = "cross"
            else:
                if opt[i+1][j] >= opt[i][j+1]:
                    opt[i+1][j+1] = opt[i+1][j]
                    pi[i+1][j+1] = "left"
                else:
                    opt[i+1][j+1] = opt[i][j+1]
                    pi[i+1][j+1] = "up"

    return (opt,pi)

def getSequence(A,B,pi):
    i,j = len(A),len(B)
    res = ""
    while i>0 and j>0:
        if pi[i][j] == "cross":
            res+=A[i-1]
            i-=1
            j-=1
        else:
            if pi[i][j] == "up":
                i-=1
            else:
                j-=1
    return res[::-1]

A = input()
B = input()
opt,pi = lcs(A,B)
length = opt[len(A)][len(B)]
seq = getSequence(A,B,pi)

print(length)
print(seq)


