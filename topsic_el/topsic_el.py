#品切れ
N = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))

item = 0
aaa = 0
#print(A,B)
for i in range(N):
     if A[i] >= B[i]:
         aaa = 1
     if A[i] < B[i]:
         item = A[i]
print(A.index(item)+1)  