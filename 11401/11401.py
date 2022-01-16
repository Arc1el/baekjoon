p = 1000000007
values = input()
values = values.split()
n = int(values[0])
k = int(values[1])

def solution(a, b):
    if(b % 2 > 0):
        return solution(a, b - 1) * a
    elif(b == 1):
        return a
    elif(b == 0):
        return 1
    else:
        result = solution(a, b//2)
        return result ** 2 % p
    
facto_n = 1
facto_k = 1
facto_nk = 1
    
for num in range(1, n+1): 
    facto_n = facto_n * num
    facto_n = facto_n % p

for num in range(1, k+1):
    facto_k = facto_k * num
    facto_k = facto_k % p
    
for num in range(1, n-k+1):
    facto_nk = facto_nk * num
    facto_nk = facto_nk % p
    
deno = solution(facto_k * facto_nk, p-2) % p
result = (facto_n * deno) % p

print(result)
