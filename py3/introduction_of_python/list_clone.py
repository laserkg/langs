# encoding: utf-8


def remove_dups(L1, L2):
    """
    假设L1和L2是列表，删除L2中出现的L1中的元素
    """
    for e1 in L1:
        # for e1 in L1[:]:
        if e1 in L2:
            L1.remove(e1)


L1 = [1, 2, 3, 4]
L2 = [1, 2, 5, 6]
remove_dups(L1, L2)
print('L1 =', L1)  # L1 = [2, 3, 4]
