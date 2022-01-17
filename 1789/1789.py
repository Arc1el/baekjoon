max = int(input())

n = 1
while True:
    sum = n * (n+1) / 2

    if sum > max:
        print(n-1)
        break
    else:
        n += 1
