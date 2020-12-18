

def is_even(a):
    if a % 2 == 0:
        return True
    else:
        return False

#    while a != and a !=0:
#        a // 2
#        if a == 0:
#            return True
#        elif a == 1:
#            return False



print(is_even(5)) # Falese
print(is_even(6)) # True
print(is_even(0)) # True
print(is_even(7)) # Type Error


def opposite(a,b):
    if a > 0 and b < 0:
        return True
    elif a < 0 and b > 0:
        return True
    else:
        return False


print(opposite(10, -1)) # True
print(opposite(2, 3)) # False



def near_100(num):
   # if num <= 110 and num >= 90:
   #     return True
   # else:
   #     return False

    if num in range(90, 111):
        return True
    else:
        return False

print(near_100(50)) # False
print(near_100(99)) # True
print(near_100(105)) # True


def maximum_of_threat(a, b, c):
    if a > b:
        if a > c:
            return a
        else:
            return c
    elif b> a:
        if b> c:
            return b
        else:
            return c
    else:
        if a > c:
            return c
        else:
            return c

print(maximum_of_threat(5,6,2))
print(maximum_of_threat(-4,3,10))    
print(maximum_of_threat(4,4,8))




