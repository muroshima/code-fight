#S = list(map(str,input()))
#A =[0,0,0,0,0,0,0,0,0,0]
#B = ["a","s","d","f","g","h","j","k","l"]

#lists = list(zip(A,B))
#print (lists)

#tile = [0] * N

#kazu = len(S)

#print = (S)
#for i in range(1, kazu):
 #   tile[i] = min(tile[i-1] + 1)
#print(tile[-1])



#for i in range(3):
 #   A.append([1, 1, 1])
#for j in range(10):
 #   A.append([1, 1, 1,1,1,1,1,1,1,1])


#A[0][0],A[0][1],A[0][2] = map(int, input().split())

#for i in range(3):
 #   for j in range(10):
 #       A[i][j] += A[i-1][j]
        
 #       if j-1 >= 0:
  #          A[i][j] += A[i-1][j-1]

  #      if j+1 < 4:
  #          A[i][j] += A[i-1][j+1]

#print(A[3][3]+1)


#S = input()
#kazu = len(S)

#for i in range(kazu):
 #    if kazu[i] == "a":
  #       kazu[i] = 1
   #  elif kazu[i] == "A":
    #     kazu[i] = 1

     #elif kazu[i] == "s":
      #   kazu[i] =2
     #elif kazu[i] == "S":
      #   kazu[i] = 2

     #elif kazu[i] == "d":
      #   kazu[i] = 3
     #elif kazu[i] == "D":
      #   kazu[i] = 3

    # elif kazu[i] == "f":
    #     kazu[i] = 4
    # elif kazu[i] == "F":
    #     kazu[i] = 4
    
    # elif kazu[i] == "g":
    #     kazu[i] = 5
    # elif kazu[i] == "G":
    #     kazu[i] = 5

   #  elif kazu[i] == "h":
    #     kazu[i] = 6
  #   elif kazu[i] == "H":
   #      kazu[i] = 6
    
    # elif kazu[i] == "j":
    #     kazu[i] = 7
   #  elif kazu[i] == "J":
    #     kazu[i] = 7
    
   #  elif kazu[i] == "k":
    #     kazu[i] = 8
   #  elif kazu[i] == "K":
   #      kazu[i] = 8

    # elif kazu[i] == "l":
    #     kazu[i] = 9
   #  elif kazu[i] == "L":
    #     kazu[i] = 9
   #  else:
    #     print("No")

#aaa=kazu[0]

#for j in range(1, len(kazu)):
 #   aaa += abs(kazu[j] - kazu[i]) + 1

#print(aaa) 



word=list(input())
klist=list("asdfghjkl")
pos=0
#総秒数
ppos = 0
#前の場所
mov=0
#移動量
for i in word:
    mov=abs(klist.index(i)-ppos)
    pos=pos+mov+1
    ppos=klist.index(i)
print(pos)