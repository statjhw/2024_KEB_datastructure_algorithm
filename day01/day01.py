import mymath
import time
import random

count = 7
rand = random.randint(0,100)
while  count != 0:
    count -= 1
    n = int(input("숫자를 입력하세요 : "))
    if n == rand:
        print("정답입니다.")
        print(f"{7-count}번 실행했습니다.")
        break
    elif n > rand :
        print(f"{n}보다 작은 수 입니다.")
    else :
        print(f"{n}보다 큰 수입니다.")
else :
    print("주어진 기회를 모두 사용했습니다.ㅜㅜ")
