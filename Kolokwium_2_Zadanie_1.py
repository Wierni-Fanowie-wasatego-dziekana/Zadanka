# def garek(L,row,col):
#     return (row, col) in L
#
# def czy_sie_zmiesci(w,k):
#     if w > N-1 or k > N-1:
#         return False
#     return True
#
#
# def rook(N, L, w = 0, k = 0, counter = 0):
#     if (N - 1, N - 1) in L:
#         return None
#     if w == N - 1 and k == N - 1:
#         return counter

def zajete(L,row,col):
    return (row,col) in L

def rook(N,L, w = 0, k = 0, counter = 0, last =-1) : # last: prawo=0; doł=1
    if w >= N or k >= N:
        return None
    if w == N - 1 and k == N - 1:
        return counter

    # if not zajete(L, w, k):
    #     return rook(N, L, w + 1, k, counter + 1) or rook(N, L, w, k + 1, counter + 1)
    # return None

    if not zajete(L, w, k):
        pass
            # if last == -1:
            #      temp1=rook(N,L,w+1,k,counter+1,1)
            #      temp2=rook(N,L,w,k+1,counter+1,0)
            #      if temp1 is not None and temp2 is not None:
            #         return min(temp1,temp2)
            # elif last == 0:
            #      temp3=rook(N, L, w + 1, k, counter + 1,1)
            #      temp4=rook(N,L,w,k+1,counter,0)
            #      if temp3 is not None and temp4 is not None:
            #         return min(temp3,temp4)
            # elif last == 1:
            #     temp5=rook(N, L, w, k + 1, counter+1,0)
            #     temp6=rook(N,L,w+1,k,counter,1)
            #
            #     return min(temp5,temp6)

    return None
#L = [(0,3),(1,0),(1,1),(1,3),(1,4),(2,0),(3,0),(3,2),(3,3),(4,0)]
L = [(1,1),(1,2)]
#L = [(0,1),(0,4),(1,2),(1,4),(2,0),(2,5),(3,1),(3,3),(4,2),(4,4)]
print(rook(4, L))

# Wizualna prezentacja położenia pionków
# W 0 0 1 0 kutas
# 1 1 0 1 1
# 1 0 0 0 0
# 1 0 1 1 0
# 1 0 0 0 0





