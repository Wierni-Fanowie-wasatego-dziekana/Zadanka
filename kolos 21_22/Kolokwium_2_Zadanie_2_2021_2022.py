''''Aby otrzymać nagrodę trzeba przejść kolejno przez N komnat. W każdej komnacie znajduje się
skrzynia (mogąca pomieścić maksymalnie 100 sztabek), w której umieszczono pewną liczbę sztabek
złota. Będąc w danej komnacie możemy zabrać ze skrzyni pewną liczbę sztabek albo dołożyć do
skrzyni wcześniej zebrane sztabki. Liczba sztabek przenoszona do następnej komnaty nie może
przekraczać 6. Drzwi do kolejnej komnaty otwierają się wtedy, gdy liczba sztabek pozostawiona
w skrzyni będzie liczbą pierwszą. Z ostatniej komnaty nie wolno wynieść żadnej sztabki. Proszę
napisać funkcję, która zwraca informację, czy jest możliwe przejście przez komanty. Do funkcji
należy przekazać tablicę zawierającą liczby sztabek w kolejnych komnatach. Na przykład:
T = [10, 20, 30] −→ funkcja powinna zwrócić False
T = [10, 20, 35] −→ funkcja powinna zwrócić True, w komnatach pozostanie [5, 23, 37]'''''

def is_prime(n):
    if n < 2:
        return False
    if n % 2 == 0 or n % 3 == 0:
        return False
    if n == 2 or n == 3:
        return True
    i = 5
    while i * i < n:
        if n % i == 0:
            return False
        i += 2
        if n % i == 0:
            return False
        i += 4

    return True


def komnaciory(T, N, temp_N = 0, temp_gold = 0):
    if temp_N == N:
        return is_prime(T[temp_N] + temp_gold) and T[temp_N] + temp_gold <= 100
    # end if
    for i in range(temp_gold - 6, temp_gold + 1):
       if is_prime(T[temp_N] + i) and T[temp_N] < 100:
            if komnaciory(T,N, temp_N + 1, temp_gold - i):
                return True
    # end for
       #end if
            # end if
# end def

    return False



print(komnaciory([10,10,17],2))

