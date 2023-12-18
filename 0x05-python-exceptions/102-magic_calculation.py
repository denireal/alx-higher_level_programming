#!/usr/bin/python3

def magic_calculation(a, b):
    result_value = 0
    for i in range(1, 3):
        try:
            if i > a:
                raise Exception('Too far')
            result_value += a ** b / i
        except Exception as e:
            result_value = b + a
            break
    return result_value
