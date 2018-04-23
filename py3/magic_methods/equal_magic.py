# encoding: utf-8


class TNone(object):
    def __eq__(self, other):
        return False


t = TNone()
print(t == None)
print(t is None)
