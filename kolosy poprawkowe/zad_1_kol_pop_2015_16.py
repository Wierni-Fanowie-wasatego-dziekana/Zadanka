''''L Dana jest tablica int t[N][N] zawierająca liczby naturalne. Dokładnie w jednym z wierszy
 atablicy znajduje się fragment ciągu Fibonacciego o długościwiększej niż2,a mniejszej niż N. Proszę
napisać funkcję, która odszuka ten fragment ciągu i zwróci numer wiersza w którym on się znajduje.'''''

def is_fib(c,b,a):
    n1,n2 = 1, 1
    if a + b == c:
        while n2 < c:
            n1, n2 = n2, n1 + n2

        return c == n2 and b == n1
    return False


#print(is_fib(5,3,2))

def zadanie1(T):
    for row in range(len(T)):
        for col in range(2, len(T)):
            if is_fib(T[row][col], T[row][col - 1], T[row][col - 2]):
                return row
    return 'Chuj'

tablice = [[7 ,1,5,1,4],
           [10,2,2,4,1],
           [20,3,2,4,5],
           [33,5,3,3,2],
           [3 ,8,13,21,1]]

print(zadanie1(tablice))



