
achieved_goal = False
def rook(N,L, pos_y = 0, pos_x = 0, number_of_moves = 0):
    global achieved_goal

    if not (pos_x == N-1 and pos_y == N-1):
        minimal_number_of_moves = N*4
        for i in range(pos_x+1, N):
            if(pos_y,i) in L:
                break
            else:
                temp = rook(N,L,pos_y,i,number_of_moves + 1)
                if temp != None:
                    if temp < minimal_number_of_moves:
                        minimal_number_of_moves = temp
        for i in range(pos_y+1, N):
            if (i, pos_x)  in L:
                break
            else:
                temp = rook(N,L,i,pos_x,number_of_moves + 1)
                if temp != None:
                    if temp < minimal_number_of_moves:
                        minimal_number_of_moves = temp
        number_of_moves = minimal_number_of_moves

    if pos_x == N-1 and pos_y == N-1:
        achieved_goal = True

    if achieved_goal:
       return number_of_moves
    return None

L = [(0,3),(1,0),(1,1),(1,3),(1,4),(2,0),(3,0),(3,2),(3,3),(4,0)]
L2 = [(1,1),(1,2)]
L3 = [(0,1),(0,4),(1,2),(1,4),(2,0),(2,5),(3,1),(3,3),(4,2),(4,4)]
L4 = [(0,4),(1,0),(1,2),(1,4),(2,0),(2,3),(2,4),(3,0),(3,1),(3,4)]

# Wizualna prezentacja położenia pionków
# W 0 0 1 0
# 1 1 0 1 1
# 1 0 0 0 0
# 1 0 1 1 0
# 1 0 0 0 0

# W 0 0 0 1
# 1 0 1 0 1
# 1 0 0 1 1
# 1 1 0 0 1
# 0 0 0 0 0

print(rook(5,L4))