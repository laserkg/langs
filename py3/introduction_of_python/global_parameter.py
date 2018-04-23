# encoding: utf-8

global num_calls


def fib(x):
    """
    假设x是正整数，返回第x个斐波那契数
    :param x:
    :return: 第x个斐波那契数
    """
    global num_calls
    num_calls += 1

    if x == 0 or x == 1:
        return 1
    else:
        return fib(x - 1) + fib(x - 2)


num_calls = 100
fib(10)
print(num_calls)
