'''Dana jest tablica wypeªniona liczbami naturalnymi int t[N][N] reprezentuj¡ca szachownic¦. Prosz¦ napisa¢
funkcj¦, która sprawdza, czy jest mo»liwe ustawienie dwóch wzajemnie szachuj¡cych si¦ skoczków tak, aby
suma warto±ci pól, na których stoj¡ skoqczki, byªa liczb¡ pierwsz¡. Do funkcji nale»y przekaza¢ tablic¦ t,
funkcja powinna zwróci¢ warto±¢ typu bool'''''


def is_prime(n):

    # TRESC OCZYWISTA #
    if n < 4:
        return n>1
    #end if
    if n %2 ==0 or n%3==0:
        return False
    #end if
    for i in range(5,int(n**0.5+1),6):
        if n%i==0 or n%(i+2)==0:
            return False
        #end if
    #end for
    return True

#end def


def jumping_jumpers(T):

    moves = [(2,1),(2,-1),(-2,1),(-2,-1),(1,-2),(1,2),(-1,2),(-1,-2)]

    for i in range(len(T)):
        for j in range(len(T)):
            for move in moves:
                if 0 <= i + move[0] < len(T) and 0 <= j + move[1] < len(T):
                    if is_prime(T[i][j] + T[i + move[0]][j + move[1]]):
                        return True
        # end for
                # end if
                    # end if
            #end for
    # end for
    return False

# end def

T=[
    [2,2,2,2,2],
    [2,2,2,2,2],
    [2,2,2,2,2],
    [2,2,2,2,2],
    [2,2,2,2,2]
]

print(jumping_jumpers(T))