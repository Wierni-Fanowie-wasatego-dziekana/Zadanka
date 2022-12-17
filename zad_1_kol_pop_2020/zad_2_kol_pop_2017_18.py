'''Dane s¡ dwie tablice int t1[N] oraz int t2[N] wypeªnione liczbami naturalnymi. Elementy z tablic t1 i t2
ª¡czymy w pary (po jednym elemencie z ka»dej tablicy) tak, aby suma wybranych elementów z tablicy t1 byªa
równa sumie wybranych elementów z tablicy t2. Prosz¦ napisa¢ funkcj¦, która zwróci maksymaln¡ liczb¦
par, jak¡ mo»na uzyska¢. Do funkcji nale»y przekaza¢ wyª¡cznie tablice t1 i t2, funkcja powinna zwróci¢
maksymaln¡ liczb¦ par.'''''

# !!!!!!!!!!!!! #
    

def wszystkie(T):
    s = 0
    for i in range(len(T)):
        s += T[i]
    return s

def brute_force(T1,T2):
    N = len(T1)
    if wszystkie(T1) == wszystkie(T2):
        return N
    for i in range(N):
        for j in range(N):
            kopia1 = T1.copy()
            kopia2 = T2.copy()
            kopia1.pop(i)
            kopia2.pop(j)
            brute_force(kopia1,kopia2)


T1 = [2,3,4,8]
T2 = [1,5,3,9]

print(brute_force(T1,T2))

