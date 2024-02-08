import mymath
import time

if __name__ == "__main__" : #여러 개의 파일을 실행 시 메인 파일을 확인하는 코드
    # n = int(input("Input n : "))
    # r = int(input("Input r : "))
    # start = time.time()
    # print(f"{n}C{r} = {mymath.nCr(n, r)}")
    # end = time.time()
    # print(f"소요시간 : {end - start}")

    start = time.time()
    mymath.factorial(100)
    end = time.time()
    print(f"반복문 : {end - start}")

    start = time.time()
    mymath.factorial_resursion(100)
    end = time.time()
    print(f"재귀 : {end - start}")

