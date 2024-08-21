##import math
##def s(nu):
##    if nu < 2:
##        return False
##    for i in range(2,int(math.sqrt(nu))+ 1):
##        if nu % i == 0:
##            return False
##    return True
##
##def f(arr):
##    h = 0
##    for index in range(len(arr)):
##        if s(index):
##            h += arr[index]
##    return h
##
##arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
##print(f(arr))
import math
def s(nu):
    if nu < 2:
        return False
    for i in range(2,int(math.sqrt(nu))+ 1):
        if nu % i == 0:
            return False
    return True
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


h = 0
for index in range(len(arr)):
        if s(index):
            h += arr[index]
print( h)


