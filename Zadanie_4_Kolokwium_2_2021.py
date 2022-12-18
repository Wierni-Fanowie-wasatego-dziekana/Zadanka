'''W tablicy o rozmiarze N ×N wypełnionej liczbami naturalnymi umieszczono dokładnie jeden fragment 
ciągu Fibonacciego o długości co najmniej 3 elementów. Cały fragment leży w jednym z wierszy
lub kolumn w kierunku rosnącym lub malejącym. Prosze napisać funkcję, która dla zadanej tablicy
odszuka ten fragment i zwróci jego wartość.'''''

def fib(n1,n2,n3):
    # f0=0
    # f1=1
    # for i in range(n):
    #     f1,f0=f0+f1,f1
    a, b = 1,1
    if n1 + n2 == n3:
        while b < n3:
            a, b = b, a + b
        return n3 == b and n2 == a
    return False

def fib_in_array(T):
    n = len(T)
    dl = 2
    for i in range(0,n): # check rows ascending
        for j in range(2,n):
            if fib(T[i][j-2],T[i][j-1],T[i][j]):
                dl +=1
            elif dl >= 3:
                return dl
        if dl >=3:
            return dl

    for i in range(0,n): # check rows descending
        for j in range(2,n):
            if fib(T[i][j],T[i][j-1],T[i][j-2]):
                dl+=1
            elif dl >=3:
                return dl
        if dl >=3:
            return dl

    for j in range(n): # check cols ascending
        for i in range(2, n):
            if fib(T[i-2][j], T[i-1][j], T[i][j]):
                dl += 1
            elif dl >= 3:
                return dl
        if dl >= 3:
            return dl

    for j in range(n): # check cols descending
        for i in range(2, n):
            if fib(T[i][j], T[i - 1][j], T[i-2][j]):
                dl += 1
            elif dl >= 3:
                return dl
        if dl >= 3:
            return dl

    return 1

T = [
    [2,3,5,8],
    [8,7,9,5],
    [4,2,3,4],
    [6,9,8,2],
]

print(fib_in_array(T))