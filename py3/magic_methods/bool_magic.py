"""
Link: https://docs.python.org/3/reference/datamodel.html

object.__bool__(self)
    Called to implement truth value testing and the built-in operation bool(); should return False or True.
    When this method is not defined, __len__() is called, if it is defined, and the object is considered true if its result is nonzero.
    If a class defines neither __len__() nor __bool__(), all its instances are considered true.
"""


# user collection class
class UC1(object):

    def __init__(self, users):
        self._users = users


class UC2(object):

    def __init__(self, users):
        self._users = users

    # def __len__(self):
    #     print("UC2 len method")
    #     return len(self._users)
    #

    def __bool__(self):
        print("UC2 bool method")
        return True if len(self._users) > 0 else False


def test_uc1():
    users = UC1(['piglei', 'raymond'])

    if len(users._users) > 0:
        print("There's some users in collection 1!")


def test_uc2():
    users = UC2(['piglei', 'raymond'])
    # 因为有了__len__，这里可以直接对UC2对象进行bool操作了
    if users:
        print("There's some users in collection 2!")
    else:
        print("UC2 is False")


class T(object):
    def __len__(self):
        # return 0
        return 1


class T1(object):
    def __bool__(self):
        return False





if __name__ == '__main__':
    test_uc1()
    test_uc2()
    print(bool(T()))