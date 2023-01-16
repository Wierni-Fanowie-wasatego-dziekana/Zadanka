'''Dwie liczby naturalne są czynnikowo-podobne, jeżeli w swoich rozkładach na czynniki pierwsze mają
dokładnie jeden czynnik równy. Na przykład: 24 i 14 albo 32 i 18. Dana jest tablica T[N][N]
zawierająca liczby naturalne. Dwie liczby sąsiadują ze sobą wtedy, gdy leżą w sąsiednich kolumach i
sąsiednich wiersza. Proszę napisać funkcję three(T), która zwraca ilość liczb w tablicy sąsiadujących
dokładnie z 3 liczbami czynnikowo-podobnymi
'''''


def czynnikowo_podobne(a, b):
    x = 2
    cnt = 0
    while a != 1:
        while a % x == 0:
            a //= x
            if b % x == 0:
                b //= x
                cnt += 1
        x += 1

    return cnt == 1

def three(T):
    n = len(T)
    cnt = 0
    zmienna_typu_integer_zliczajaca_ilosc_liczb_ktora_ma_trzech_sasiadow_czynnikowo_podobnych_w_zadaniu_numer_jeden_z_kolokwium_numer_trzy_dla_studentow_pierwszego_semestru_informatyki_prowadzonej_na_wydziale_informatyki_elektroniki_i_telekomunikacji_stworzone_przez_prodziekana_do_spraw_ksztalcenia_oraz_opiekuna_kierunku_oraz_prowadzacego_przedmiotu_wstep_do_informatyki_doktora_Marka_Gajeckiego_z_roku_akademickiego_akademii_gorniczo_hutniczej_im_Stanislawa_Staszica_w_Krakowie_2021_2022 = 0
    moves = [(1,1),(-1,1),(1,-1),(-1,-1)]
    for row in range(1, n-1):
        for col in range(1, n - 1):
            for move in moves:
                if czynnikowo_podobne(T[row][col], T[row + move[0]][col + move[1]]):
                    cnt += 1

            if cnt == 3:
                zmienna_typu_integer_zliczajaca_ilosc_liczb_ktora_ma_trzech_sasiadow_czynnikowo_podobnych_w_zadaniu_numer_jeden_z_kolokwium_numer_trzy_dla_studentow_pierwszego_semestru_informatyki_prowadzonej_na_wydziale_informatyki_elektroniki_i_telekomunikacji_stworzone_przez_prodziekana_do_spraw_ksztalcenia_oraz_opiekuna_kierunku_oraz_prowadzacego_przedmiotu_wstep_do_informatyki_doktora_Marka_Gajeckiego_z_roku_akademickiego_akademii_gorniczo_hutniczej_im_Stanislawa_Staszica_w_Krakowie_2021_2022 += 1
            cnt = 0
    return zmienna_typu_integer_zliczajaca_ilosc_liczb_ktora_ma_trzech_sasiadow_czynnikowo_podobnych_w_zadaniu_numer_jeden_z_kolokwium_numer_trzy_dla_studentow_pierwszego_semestru_informatyki_prowadzonej_na_wydziale_informatyki_elektroniki_i_telekomunikacji_stworzone_przez_prodziekana_do_spraw_ksztalcenia_oraz_opiekuna_kierunku_oraz_prowadzacego_przedmiotu_wstep_do_informatyki_doktora_Marka_Gajeckiego_z_roku_akademickiego_akademii_gorniczo_hutniczej_im_Stanislawa_Staszica_w_Krakowie_2021_2022
