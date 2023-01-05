''' Dana jest tablica int t[9], w której nale»y umie±ci¢ liczby od 1 do 9 tak, aby byªy speªnione warunki:
1) warto±ci na s¡siednich polach tablicy musz¡ si¦ ró»ni¢ o co najmniej 2
2) liczby pierwsze nie mog¡ zajmowa¢ s¡siednich pól tablicy
Warto±¢ 1 zostaªa ju» umieszczona w pierwszym (pod indeksem 0) elemencie tablicy. Prosz¦ napisa¢ program,
który wypisuje wszystkie poprawne rozmieszczenia liczb w tablicy.'''''

def is_2_or_3_or_5_or_7(n):
    return n == 2 or n == 3 or n == 5 or n == 7

def warunek_1(T, a):
    return abs(T[a] - T[a + 1]) >= 2

def warunek_2(T, a):
    return is_2_or_3_or_5_or_7(T[a]) and is_2_or_3_or_5_or_7(T[a+1]) 

def zadanie(T, i=1):
    if i == len(T):
        print(T)
        return

    for j in range(2,len(T)+1):
        if j not in T:
            T[i] = j
            if warunek_1(T, i-1) and not warunek_2(T, i-1):
                zadanie(T, i+1)
            T[i] = 0

tablica_wejsciowa = [1,0,0,0,0,0,0,0,0]

zadanie(tablica_wejsciowa)