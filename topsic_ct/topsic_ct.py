N = int(input())
D = [int(input()) for _ in range(1,N+1)]
#print(D)

X = sum(D[::4]) - sum(D[2::4])
Y = sum(D[3::4]) - sum(D[1::4])

print(X,Y)   