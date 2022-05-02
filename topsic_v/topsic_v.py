N = int(input())
fluits = list(map(str,input()))

box_count = 0

for i in range(1, N):
    if fluits[i-1] != fluits[i]:
        box_count += 1
    else:
        box_count += 0

print(box_count+1)  