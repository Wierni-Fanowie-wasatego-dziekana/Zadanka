
def one_is_biggest_divider_of_three(a,b,c):
    a1,b1,c1 = a, b, c
    while b1 > 0:
        a1, b1 = b1, a1 % b1
    if a1 != 1:
        return False

    a2, b2, c2 = a, b ,c
    while a2 >0:
        c2, a2 = a2, c2 % a2
    if c2 != 1:
        return False

    while b > 0:
        c, b = b, c % b
    return c == 1

def trojki(T):
    def iterate(counter = 0):

        if len(T) < 3:
            return 0

        for i in range(0,len(T)):
            if i + 2 < len(T) and one_is_biggest_divider_of_three(T[i],T[i + 1],T[i + 2]):
                counter += 1
            if i + 3 < len(T) and one_is_biggest_divider_of_three(T[i], T[i + 2], T[i + 3]):
                counter += 1
            if i + 3 < len(T) and one_is_biggest_divider_of_three(T[i], T[i + 1],T[i + 3]):
                counter += 1
            if i + 4 < len(T) and one_is_biggest_divider_of_three(T[i],T[i + 2],T[i + 4]):
                counter += 1

        return counter

    return iterate()

print(trojki([2,4,6,7,8,10,12])) # 0 trójek
print(trojki([2,3,4,6,7,8,10])) # 1 trójka (3,4,7)
print(trojki([2,4,3,6,5])) # 2 trójki (2,3,5),(4,3,5)
print(trojki([2,3,4,5,6,8,7])) # 5 trójek (2,3,5),(3,4,5),(3,5,8),(5,6,7),(5,8,7)