#約数の総和
num = int (input())
answer = [i for i in range(1, num+1) if num % i ==0]
print(sum(answer))