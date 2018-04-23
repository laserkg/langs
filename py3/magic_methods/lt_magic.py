# encoding: utf-8
class T(object):
    def __init__(self, c):
        self.code = c

    def __lt__(self, other):
        print("__lt__")
        return False

    # def __gt__(self, other):
    #     print('__gt__')
    #     return True


t1 = T(1)
t2 = T(2)

if t1 < t2:
    print("t1(%s): less than t2(%s)" % (t1.code, t2.code))
else:
    print("t1(%s): greater than t2(%s)" % (t1.code, t2.code))

if t1 > t2:
    print("t1(%s): less than t2(%s)" % (t1.code, t2.code))
else:
    print("t1(%s): greater than t2(%s)" % (t1.code, t2.code))
