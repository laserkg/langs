# encoding: utf-8
import copy


class Common(object):
    """
    https://docs.python.org/3/library/copy.html

    Two problems often exist with deep copy operations that don’t exist with shallow copy operations:

        * Recursive objects (compound objects that, directly or indirectly, contain a reference to themselves) may cause a recursive loop.
        * Because deep copy copies everything it may copy too much, such as data which is intended to be shared between copies.

    https://www.geeksforgeeks.org/copy-python-deep-copy-shallow-copy/
    """

    def __init__(self, names):
        self.names = names

    def add(self, name):
        self.names.append(name)

    def __str__(self):
        return ','.join(self.names)

    def __eq__(self, other):
        return self.names == other.names


class Shallow(Common):
    def __init__(self, names):
        super(Shallow, self).__init__(names)

    def __copy__(self):
        # 这种方式，返回的是同一个对象的地址
        print('__copy__')
        return self


class Deep(Common):
    def __int__(self, names):
        super(Deep, self).__init__(names)
    #
    # def __deepcopy__(self, memodict={}):
    #     print('__deepcopy__')
    #     return self


names = ['Jordon', 'Jonathon']
name = 'Kobe'


def test_common(names):
    s1 = Common(names)
    s2 = copy.copy(s1)

    s2.add(name)

    print('s1: ', s1)  # Jordon,Jonathon,Kobe
    print('s2: ', s2)  # Jordon,Jonathon,Kobe
    assert s1 == s2
    print(id(s1), id(s2))
    # 这里不成立，看来类有默认的__copy__方法，会创建新的对象
    # assert s1 is s2


def test_shallow(names):
    s1 = Shallow(names)
    s2 = copy.copy(s1)
    # s2 = s1  # 这种方法并不会调用__copy__方法

    # modify
    s2.add(name)

    print('s1: ', s1)  # Jordon,Jonathon,Kobe
    print('s2: ', s2)  # Jordon,Jonathon,Kobe
    assert s1 == s2
    assert s1 is s2


def test_deep(names):
    s1 = Deep(names)
    s2 = copy.deepcopy(s1)

    # modify
    s2.add(name)

    print('s1: ', s1)  # Jordon,Jonathon
    print('s2: ', s2)  # Jordon,Jonathon,Kobe
    assert s1 != s2
    assert s1 is not s2


if __name__ == '__main__':
    # 传入names的副本
    test_common(names[:])

    test_shallow(names[:])

    test_deep(names[:])
