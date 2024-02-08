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