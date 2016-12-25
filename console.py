import closure
import numpy
import sys

s = input('Please enter array in one line:\n>>>')


def inarray(a):
    m = []
    count = 0
    for i in s.split():
        count += 1
        m.append(int(i))

    return numpy.array(m).reshape(int(count**0.5), int(count**0.5))


def outarray(ans):
    for i in range(len(ans)):
        print(ans[i])


b = inarray(s)
ans = closure.transitive_closure(b)
outarray(ans)
if input('anykey to quit'):
    sys.exit()