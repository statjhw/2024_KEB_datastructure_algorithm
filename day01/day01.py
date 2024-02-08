import mymath
import time
import random

## 선형 리스트
#응용 : 다항식
def print_poly(f_x) -> str:
    term = len(f_x) - 1
    poly_expression = "f(x) = "

    for i in range(len(fx)):
        coefficient = f_x[i]
        if coefficient == 0 :
            term = term - 1
            continue
        if coefficient > 0 & i != 0:
            poly_expression = poly_expression + "+"
        poly_expression = poly_expression + f'{coefficient}x^{term} '
        term = term - 1

    return poly_expression


def calculation_poly(x_value, f_x) -> int:
    return_value = 0
    term = len(f_x) - 1

    for i in range(len(fx)):
        coefficient = f_x[i]
        return_value += coefficient * pow(x_value, term)
        term = term - 1

    return return_value


fx = [2, 3, 4, 0, -9]

if __name__ == "__main__":
    print(print_poly(fx))
    print(calculation_poly(int(input("x 값 : ")), fx))