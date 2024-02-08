def factorial(number) -> int :
    pass

def nCr(n, r) -> int :
    """
    조합 함수
    :param n:
    :param r:
    :return: 정수
    """
    numerator = factorial(n)
    denominator = factorial(n-r) * factorial(r)
    return numerator / denominator

if __name__ == "__main__" : #여러 개의 파일을 실행 시 메인 파일을 확인하는 코드
    n = int(input("Input n : "))
    r = int(input("Input r : "))
    print(f"{n}C{r} = {nCr(n, r)}")

