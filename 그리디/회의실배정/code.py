# 회의 개수 입력
n = int(input())

arr = []

# 회의 시간 정보를 입력받아 리스트로 구현
for _ in range(n):
    arr.append(list(map(int, input().split())))

end_day = 0
count = 0

# 회의 시간 정보를 정렬 ( 끝나는 날짜가 짧은 순으로 정렬한 후 시작 날짜가 짧은 순으로 정렬)
arr.sort(key=lambda x: (x[1], x[0]))
    
for i in range(len(arr)):
    # 현재 날짜가 다음 회의 시작날짜와 같거나 작으면
    if end_day <= arr[i][0]:
        # 회의 종료 날짜를 업데이트
        end_day = arr[i][1]
        count += 1

print(count)