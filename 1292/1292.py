a, b = map(int, input().split())

cnt = 0
total = 0
i = 1

while True:
    for j in range(i):
        if cnt + 1 >= a:
            total += i

        cnt += 1
        if cnt == b:
            break
    
    if cnt == b:
        break
    else:
        i += 1


print (total)
