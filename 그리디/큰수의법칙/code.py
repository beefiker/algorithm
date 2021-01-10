n, m, k = map(int, input().split())

data = list(map(int, input().split()))

result = 0

data.sort()
first = data[len(data)-1]
second = data[len(data)-2]

while True:
    for i in range(k):
        if m == 0: break
        result += first
        m -= 1

    if m == 0: break

    result += second
    m -= 1

print(result)
