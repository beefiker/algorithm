# 📒 Coding Note



## 📋 목차 

1. [그리디](그리디/)

   1. [거스름돈](그리디/거스름돈)
   2. [큰 수의 법칙](그리디/큰수의법칙)
   3. [숫자카드게임](그리디/숫자카드게임)
   4. [1이 될 때까지](그리디/1이될때까지)

   

2. [구현](구현/)
   1. [상하좌우](구현/상하좌우)
   2. [시각](구현/시각)
   3. [왕실의 나이트](구현/왕실의나이트)



## 👋 문제 풀이 전에 알면 좋은 함수

1. ### lambda

   람다 형식은 함수를 딱 한 줄만으로 만들게 해준다.

   + 사용예제

     ```python
     lambda 인자 : 표현식
     
     def hap(x, y):
       return x + y
     
     hap(10, 20) # result : 30
     
     (lambda x, y : x + y)(10, 20) # result : 30
     ```

     

2. ### map

   map의 첫 번째 파라미터는 함수, 두 번째로는 iterable이 들어간다.

   그리고 iterable 데이터를 첫 번째 인자인 함수에 각각 전달하여 결과값을 받는다.

   - 사용예제

     ``` python
     map(function_to_use, list_of_inputs)
     
     # 띄어쓰기로 input되는 정수 값 두개를 받는 변수
     a, b = map(int, input().split()) 
     
     # 1부터 5까지 거듭제곱의 값을 구해 리스트로 받기
     power = list(map(lambda x: x ** 2, range(1,6)))
     # Output : [1, 4, 9, 16, 25]
     ```

     

3. ### filter

   조건이 True인 요소들만 모아준다. 내장 함수여서 속도가 빠르다.

   - 사용예제

     ```python
     numbers = range(-5, 5)
     negative_nums = list(filter(lambda x: x < 0, numbers))
     print(negative_nums)
     # Output : [-5, -4, -3, -2, -1]
     ```

     



