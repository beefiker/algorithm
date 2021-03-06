# 📒 Coding Note / 그리디 - 큰 수의 법칙



+   ### 💯 큰 수의 법칙

    > + #### 문제 설명
    >
    >   다양한 수로 이루어진 배열이 있을 때 `주어진 수들을 M번 더하여 가장 큰 수`를 만드는 법칙
    >
    >   배열의 `특정한 인덱스(번호)에 해당하는 수가 연속해서 K번을 초과하여 더해질 수 없는 것`이 특징
    >
    > 
    >
    >   ***입력 조건***
    >
    >   > 첫째 줄에 N, M, K의 자연수가 주어지며, 각 자연수는 공백으로 구분한다.
    >   >
    >   > 둘째 줄에 N개의 자연수가 주어진다.각 자연수는 공백으로 구분한다. 단, 각각의 자연수는 1 이상 10,000이하의 수로 주어진다.
    >   >
    >   > 입력으로 주어지는 K는 항상 M보다 작거나 같다.
    >
    > 
    >
    >   ***출력 조건***
    >
    >   > 첫째 줄에 큰 수의 법칙에 따라 더해진 답을 출력한다.
    >
    > 
    >
    >   - ##### 예시
    >
    >     > 순서대로 `2, 4, 5, 4, 6으로 이루어진 배열`이 있다.
    >     >
    >     > `M(더할 횟수)은 8,  K(연속으로 더할 수 있는 횟수)는 3`이라고 가정한다.
    >     >
    >     > 이 경우 특정한 인덱스의 수가 연속해서 3번까지만 더해질 수 있으므로 결과는
    >     >
    >     > `6+6+6+5+6+6+6+5` 인 46이 된다.
    >
    > + #### 코드
    >
    >   ``` python
    >   n, m, k = map(int, input().split())
    >   
    >   data = list(map(int, input().split()))
    >   
    >   result = 0
    >   
    >   data.sort()
    >   first = data[len(data)-1]
    >   second = data[len(data)-2]
    >   
    >   while True:
    >       for i in range(k):
    >           if m == 0: break
    >           result += first
    >           m -= 1
    >   
    >       if m == 0: break
    >   
    >       result += second
    >       m -= 1
    >   
    >   print(result)
    >   ```
    >
    > + #### 문제 해설
    >
    >   입력값 중 가장 큰 수와 두 번째로 큰 수만 저장하면 된다.    
    >
    >   연속으로 더할 수 있는 횟수는 최대 K번이므로,   
    >
    >    `가장 큰 수를 K번 더하고 두 번째로 큰 수를 한번 더하기` 하면 된다.   
    >
    > 

    





​		