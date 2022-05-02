#約数の総和

N = int(input())

count = 0

for i in range(1, N + 1):
    for j in range(1, N + 1):
       if i % j == 0 :
         count += j

print(count) 

 
