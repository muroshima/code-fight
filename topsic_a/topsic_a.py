#小銭の組み合わせ
N = int(input())
kazu = 0
kazu2 = 0
nokori =0

a = N//100
b = N//500

if N//100 == 0:
    kazu = N//500
    nokori = N%500 
 #   print(kazu)
 #   print(nokori)
    kazu2 = nokori//100
    print(kazu2 + kazu)
else:
 print(-1)
 