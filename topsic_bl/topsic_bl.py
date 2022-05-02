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

