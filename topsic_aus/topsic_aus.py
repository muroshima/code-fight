#ジャングルジム

N = int(input())
A = list(map(int,input().split()))

for i in range(N):
    T = max(0,A[i])
print(T)