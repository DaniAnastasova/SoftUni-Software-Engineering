n = int(input())
m  = 0
for i in range(0, n+1):
    if m% 2 == 0:
        print(2 ** m)
    m+=1