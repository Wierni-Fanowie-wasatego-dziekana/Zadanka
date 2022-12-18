'''Dana jest tablica int t[N] wypeªniona liczbami caªkowitymi. Prosz¦ napisa¢ funkcj¦, która sprawdza, czymo»liwe jest "poci¦cie" tablicy na co najmniej 2 kawaªki o jednakowych sumach elementów. Do funkcji nale»yprzekaza¢ tablic¦, funkcja powinna zwróci¢ najwi¦ksz¡ liczb¦ kawaªków, na któr¡ mo»na poci¡¢ tablic¦, lubwarto±¢ 0, je±li takie poci¦cie nie jest mo»liwe. Na przykªad: dla tablicy [1,2,3,1,5,2,2,2,6] odpowiedzipowinno by¢ 4, bo [1,2,3|1,5|2,2,2|6].''''' \
def per_rectum(T, przegrodki, tablica=None, obecny_element=0): #przez odbyt
    n = len(T)
    tablica = [0 for _ in range(przegrodki)]
    for slices in range(n,1,-1):

        # TODO: zrobmy to jutro

T = [0]
per_rectum(T, len(T))
