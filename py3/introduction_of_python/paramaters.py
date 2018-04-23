# encoding: utf-8


def print_name(first_name, last_name, reverse):
    """
    输出用户的名字的格式
    :param first_name:
    :param last_name:
    :param reverse:
    :return:
    """
    if reverse:
        print(last_name, ',', first_name)
    else:
        print(first_name, last_name)


print_name('Olga', 'Puchmajervoa', False)
print_name('Olga', 'Puchmajervoa', reverse=False)
print_name(last_name='Puchmajervoa', first_name='Olga', reverse=False)
# print_name(last_name='Puchmajervoa', first_name='Olga', False)
# 输出结果是一样

