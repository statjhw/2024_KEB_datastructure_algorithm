import time
def timer(func) :
    def wrapper(*args, **kwargs) :
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"소요시간 : {end - start}")
        return result
    return wrapper


def factorial(number) -> int :
    result = 1
    for i in range(1, number+1) :
        result *= i
    return result

def factorial_resursion(number) -> int :
    if number == 1 :
        return 1
    else :
        return factorial_resursion(number-1) * number



#데코레이터를 이용해 시간을 출력
@timer
def nCr(n, r) -> int :
    """
    조합 함수
    :param n:
    :param r:
    :return: 정수
    """
    numerator = factorial_resursion(n)
    denominator = factorial_resursion(n-r) * factorial_resursion(r)
    return int(numerator / denominator)