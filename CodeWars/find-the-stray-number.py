# You are given an odd-length array of integers, in which all of them are the same, except for one single number.
# Complete the method which accepts such an array, and returns that single different number.

def stray(l):
    return l[[l.count(i) for i in l].index(1)]
