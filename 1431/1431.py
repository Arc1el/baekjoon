def solution(num):
    result = 0
    for i in num:
        if i.isdigit():
            result += int(i)
    return result


num = int(input())
result = []

for i in range(num):
    tmp = input()
    result.append(tmp)


result.sort(key = lambda x:(len(x), solution(x), x))

for i in result:
    print(i)
