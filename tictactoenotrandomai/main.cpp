#pragma clang diagnostic push
#pragma ide diagnostic ignored "readability-misleading-indentation"
#pragma ide diagnostic ignored "bugprone-branch-clone"
#pragma ide diagnostic ignored "clion-misra-cpp2008-7-3-4"
#pragma ide diagnostic ignored "clion-misra-cpp2008-6-3-1"
#pragma ide diagnostic ignored "clion-misra-cpp2008-6-4-2"
#include <iostream>
#include <iomanip>
#include <ctime>
using namespace std;
int game[3][3];
char symbols[3] = {'9', 'O', 'X'};
void board() {
    for (auto & i : game)cout << setw(3) << symbols[i[0]] << setw(3) << symbols[i[1]] << setw(3) << symbols[i[2]] << endl;
}
int main() {
    int movex, movey, difficulty, capability, round = 0;
    cout << "Select difficulty from 0 to 100 with 0 being totally random and 100 impossible.";
    cin >> difficulty;
    while(difficulty > 100 || difficulty < 0){
        cout <<"Invalid difficulty, try again" << endl;
        cin >> difficulty;
    }
    while(true) {
        board();
        cout << "What's your move, player A?";
        cin >> movey >> movex;
        round++;
        while (!(movey >= 0 && movey <= 2 && movex >= 0 && movex <= 2) || game[movey][movex] != 0) {
            cout << "Invalid coordinates, try again";
            cin >> movey >> movex;
        }
        game[movey][movex] = 1;
        board();
        if ((game[0][0] == 1 && game[0][1] == 1 && game[0][2] == 1) ||
            (game[1][0] == 1 && game[1][1] == 1 && game[1][2] == 1) ||
            (game[2][0] == 1 && game[2][1] == 1 && game[2][2] == 1) ||
            (game[0][0] == 1 && game[1][1] == 1 && game[2][2] == 1) ||
            (game[0][2] == 1 && game[1][1] == 1 && game[2][0] == 1) ||
            (game[0][0] == 1 && game[1][0] == 1 && game[2][0] == 1) ||
            (game[0][1] == 1 && game[1][1] == 1 && game[2][1] == 1) ||
            (game[0][2] == 1 && game[1][2] == 1 && game[2][2] == 1)) {
            cout << "Player A wins!";
            return 0;
        } else if (game[0][0] != 0 && game[0][1] != 0 && game[0][2] != 0 &&
                   game[1][0] != 0 && game[1][1] != 0 && game[1][2] != 0 &&
                   game[2][0] != 0 && game[2][1] != 0 && game[2][2] != 0) {
            cout << "DRAW";
            return 0;
        }
        srand(time(nullptr));
        cout << "Computer's round" << endl;
        capability = rand() % 101;
        if(difficulty == 0){
            movey = rand() % 3;
            movex = rand() % 3;
            while (!(movey >= 0 && movey <= 2 && movex >= 0 && movex <= 2) || game[movey][movex] != 0) {
                movey = rand() % 3;
                movex = rand() % 3;
            }
            }
        else if(capability <= difficulty) {
                if (game[0][0] == 2 && game[0][1] == 2 && game[0][2]==0) {
                    movey = 0;
                    movex = 2;
                } else if (game[0][1] == 2 && game[0][2] == 2 && game[0][0]==0) {
                    movey = 0;
                    movex = 0;
                } else if (game[1][0] == 2 && game[1][1] == 2 && game[1][2]==0) {
                    movey = 1;
                    movex = 2;
                } else if (game[1][1] == 2 && game[1][2] == 2 && game[1][0]==0) {
                    movey = 1;
                    movex = 0;
                } else if (game[2][0] == 2 && game[2][1] == 2 && game[2][2]==0) {
                    movey = 2;
                    movex = 2;
                } else if (game[2][1] == 2 && game[2][2] == 2 && game[2][0]==0) {
                    movey = 2;
                    movex = 0;
                } else if (game[0][0] == 2 && game[1][0] == 2 && game[2][0]==0) {
                    movey = 2;
                    movex = 0;
                } else if (game[1][0] == 2 && game[2][0] == 2 && game[0][0]==0) {
                    movey = 0;
                    movex = 0;
                } else if (game[0][1] == 2 && game[1][1] == 2 && game[2][1]==0) {
                    movey = 2;
                    movex = 1;
                } else if (game[1][1] == 2 && game[2][1] == 2 && game[0][1]==0) {
                    movey = 0;
                    movex = 1;
                } else if (game[0][2] == 2 && game[1][2] == 2 && game[2][2]==0) {
                    movey = 2;
                    movex = 2;
                } else if (game[1][2] == 2 && game[2][2] == 2 && game[0][2]==0) {
                    movey = 0;
                    movex = 2;
                } else if (game[0][0] == 2 && game[1][1] == 2 && game[2][2]==0) {
                    movey = 2;
                    movex = 2;
                } else if (game[1][1] == 2 && game[2][2] == 2 && game[0][0]==0) {
                    movey = 0;
                    movex = 0;
                } else if (game[1][1] == 2 && game[0][2] == 2 && game[2][0]==0) {
                    movey = 2;
                    movex = 0;
                } else if (game[1][1] == 2 && game[2][0] == 2 && game[0][2]==0) {
                    movey = 0;
                    movex = 2;
                } else if(game[0][0] == 2 && game[0][2] == 2 && game[0][1]==0){
                    movey = 0;
                    movex = 1;
                } else if(game[0][0] == 2 && game[2][0] == 2 && game[1][0]==0){
                    movey = 1;
                    movex = 0;
                } else if(game[0][0] == 2 && game[2][2] == 2 && game[1][1]==0){
                    movey = 1;
                    movex = 1;
                } else if(game[0][2] == 2 && game[2][0] == 2 && game[1][1]==0){
                    movey = 1;
                    movex = 1;
                } else if(game[0][2] == 2 && game[2][2] == 2 && game[1][2]==0){
                    movey = 1;
                    movex = 2;
                } else if(game[0][1] == 2 && game[2][1] == 2 && game[1][1]==0){
                    movey = 1;
                    movex = 1;
                } else if(game[1][0] == 2 && game[1][2] == 2 && game[1][1]==0){
                    movey = 1;
                    movex = 1;
                } else if(game[2][0] == 2 && game[2][2] == 2 && game[2][1]==0){
                    movey = 2;
                    movex = 1;
                } else if (game[0][0] == 1 && game[0][1] == 1 && game[0][2]==0) {
                    movey = 0;
                    movex = 2;
                } else if (game[0][1] == 1 && game[0][2] == 1 && game[0][0]==0) {
                    movey = 0;
                    movex = 0;
                } else if (game[1][0] == 1 && game[1][1] == 1 && game[1][2]==0) {
                    movey = 1;
                    movex = 2;
                } else if (game[1][1] == 1 && game[1][2] == 1 && game[1][0]==0) {
                    movey = 1;
                    movex = 0;
                } else if (game[2][0] == 1 && game[2][1] == 1 && game[2][2]==0) {
                    movey = 2;
                    movex = 2;
                } else if (game[2][1] == 1 && game[2][2] == 1 && game[2][0]==0) {
                    movey = 2;
                    movex = 0;
                } else if (game[0][0] == 1 && game[1][0] == 1 && game[2][0]==0) {
                    movey = 2;
                    movex = 0;
                } else if (game[1][0] == 1 && game[2][0] == 1 && game[0][0]==0) {
                    movey = 0;
                    movex = 0;
                } else if (game[0][1] == 1 && game[1][1] == 1 && game[2][1]==0) {
                    movey = 2;
                    movex = 1;
                } else if (game[1][1] == 1 && game[2][1] == 1 && game[0][1]==0) {
                    movey = 0;
                    movex = 1;
                } else if (game[0][2] == 1 && game[1][2] == 1 && game[2][2]==0) {
                    movey = 2;
                    movex = 2;
                } else if (game[1][2] == 1 && game[2][2] == 1 && game[0][2]==0) {
                    movey = 0;
                    movex = 2;
                } else if (game[0][0] == 1 && game[1][1] == 1 && game[2][2]==0) {
                    movey = 2;
                    movex = 2;
                } else if (game[1][1] == 1 && game[2][2] == 1 && game[0][0]==0) {
                    movey = 0;
                    movex = 0;
                } else if (game[1][1] == 1 && game[0][2] == 1 && game[2][0]==0) {
                    movey = 2;
                    movex = 0;
                } else if (game[1][1] == 1 && game[2][0] == 1 && game[0][2]==0) {
                    movey = 0;
                    movex = 2;
                }  else if(game[0][0] == 1 && game[0][2] == 1 && game[0][1]==0){
                    movey = 0;
                    movex = 1;
                } else if(game[0][0] == 1 && game[2][0] == 1 && game[1][0]==0){
                    movey = 1;
                    movex = 0;
                } else if(game[0][0] == 1 && game[2][2] == 1 && game[1][1]==0){
                    movey = 1;
                    movex = 1;
                } else if(game[0][2] == 1 && game[2][0] == 1 && game[1][1]==0){
                    movey = 1;
                    movex = 1;
                } else if(game[0][2] == 1 && game[2][2] == 1 && game[1][2]==0){
                    movey = 1;
                    movex = 2;
                } else if(game[0][1] == 1 && game[2][1] == 1 && game[1][1]==0){
                    movey = 1;
                    movex = 1;
                } else if(game[1][0] == 1 && game[1][2] == 1 && game[1][1]==0){
                    movey = 1;
                    movex = 1;
                } else if(game[2][0] == 1 && game[2][2] == 1 && game[2][1]==0){
                    movey = 2;
                    movex = 1;
                } else if (round == 2 && ((game[0][0] == 1 && game[2][2] == 1) || (game[0][2] == 1 && game[2][0] == 1))){
                    if(game[0][1] == 0){
                        movey=0;
                        movex=1;
                    } else if(game[1][0] == 0){
                        movey=1;
                        movex=0;
                    } else if(game[1][2] == 0){
                        movey=1;
                        movex=2;
                    } else if(game[2][1] == 0){
                        movey=2;
                        movex=1;
                    }
                } else if (round == 1 && (game[0][0] == 1 ||
                                          game[0][2] == 1 ||
                                          game[2][0] == 1 ||
                                          game[2][2] == 1)) {
                    movey = 1;
                    movex = 1;
                } else if (game[1][1] == 0) {
                    movey = 1;
                    movex = 1;
                } else if (game[1][1] == 1 && round == 1){
                    if(game[0][0] == 0){
                        movey = 0;
                        movex = 0;
                    }
                    else if(game[0][2] == 0){
                        movey = 0;
                        movex = 2;
                    }
                    else if(game[2][2] == 0){
                        movey = 2;
                        movex = 2;
                    }
                    else if(game[2][0] == 0){
                        movey = 2;
                        movex = 0;
                    }
                } else if (game[0][0] == 1 && game[0][2] == 1 && game[0][1] == 0) {
                    movey = 0;
                    movex = 1;
                } else if (game[0][0] == 1 && game[2][0] == 1 && game[1][0] == 0) {
                    movey = 1;
                    movex = 0;
                } else if (game[0][2] == 1 && game[2][2] == 1 && game[1][2] == 0) {
                    movey = 1;
                    movex = 2;
                } else if (game[2][0] == 1 && game[2][2] == 1 && game[2][1] == 0) {
                    movey = 2;
                    movex = 1;
                } else if (game[0][1] == 1 && game[1][0] == 1 && game[0][0] == 0){
                    movey = 0;
                    movex = 0;
                } else if (game[0][1] == 1 && game[1][2] == 1 && game[0][2] == 0){
                    movey = 0;
                    movex = 2;
                } else if (game[1][2] == 1 && game[2][1] == 1 && game[2][2] == 0){
                    movey = 2;
                    movex = 2;
                } else if (game[2][1] == 1 && game[1][0] == 1 && game[2][0] == 0){
                    movey = 2;
                    movex = 0;
                } else if (game[1][1] == 2 && game[0][1] == 1){
                    if(game[1][2] == 0){
                        movey = 1;
                        movex = 2;
                    } else if(game[2][1] == 0){
                        movey = 2;
                        movex = 1;
                    } else if(game[1][0] == 0){
                        movey = 1;
                        movex = 0;
                    }
                } else if (game[1][1] == 2 && game[1][0] == 1) {
                    if (game[0][1] == 0) {
                        movey = 0;
                        movex = 1;
                    } else if (game[1][2] == 0) {
                        movey = 1;
                        movex = 2;
                    } else if (game[2][1] == 0) {
                        movey = 2;
                        movex = 1;
                    }
                } else if (game[1][1] == 2 && game[1][2] == 1) {
                    if (game[2][1] == 0) {
                        movey = 2;
                        movex = 1;
                    } else if (game[1][0] == 0) {
                        movey = 1;
                        movex = 0;
                    } else if (game[0][1] == 0) {
                        movey = 0;
                        movex = 1;
                    }
                } else if (game[1][1] == 2 && game[2][1] == 1) {
                    if (game[1][0] == 0) {
                        movey = 1;
                        movex = 0;
                    } else if (game[1][2] == 0) {
                        movey = 1;
                        movex = 2;
                    } else if (game[0][1] == 0) {
                        movey = 0;
                        movex = 1;
                    }
                }
                while (!(movey >= 0 && movey <= 2 && movex >= 0 && movex <= 2) || game[movey][movex] != 0){
                    movey = rand() % 3;
                    movex = rand() % 3;
                }
            }
        else{
            movey = rand() % 3;
            movex = rand() % 3;
            while (!(movey >= 0 && movey <= 2 && movex >= 0 && movex <= 2) || game[movey][movex] != 0) {
                movey = rand() % 3;
                movex = rand() % 3;
            }
        }


            game[movey][movex] = 2;
            if ((game[0][0] == 2 && game[0][1] == 2 && game[0][2] == 2) ||
                (game[1][0] == 2 && game[1][1] == 2 && game[1][2] == 2) ||
                (game[2][0] == 2 && game[2][1] == 2 && game[2][2] == 2) ||
                (game[0][0] == 2 && game[1][1] == 2 && game[2][2] == 2) ||
                (game[0][2] == 2 && game[1][1] == 2 && game[2][0] == 2) ||
                (game[0][0] == 2 && game[1][0] == 2 && game[2][0] == 2) ||
                (game[0][1] == 2 && game[1][1] == 2 && game[2][1] == 2) ||
                (game[0][2] == 2 && game[1][2] == 2 && game[2][2] == 2)) {
                board();
                cout << "Computer wins!";
                return 0;
            } else if (game[0][0] != 0 && game[0][1] != 0 && game[0][2] != 0 &&
                       game[1][0] != 0 && game[1][1] != 0 && game[1][2] != 0 &&
                       game[2][0] != 0 && game[2][1] != 0 && game[2][2] != 0) {
                board();
                cout << "DRAW";
                return 0;
            }
        }
}