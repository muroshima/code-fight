#ジャングルジム

N = int(input())
A = list(map(int,input().split()))

count = 0
num = 0

for i in range(1,N):
    count += max(0,A[i] - A[i-1])
#print(count)

for u in reversed(range(1,N)):
    num += max(0,-A[u] + A[u-1])
#print (num)

if count > num:
    print (num)
else: 
    print (count)

