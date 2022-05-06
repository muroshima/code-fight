#互いに異なる

N = int(input())
A = list(map(int,input().split()))
A.sort()

Ai = set(A)
Ai = list(Ai)

#print(A)
#print(Ai)

if Ai == A:
     print("YES")
else:
     print("NO") 
  