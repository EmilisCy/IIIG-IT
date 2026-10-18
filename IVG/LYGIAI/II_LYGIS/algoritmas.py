with open('IVG/LYGIAI/II_LYGIS/duomenys.txt', 'r') as failas:
    n = int(failas.readline())

    daugiausia_tasku = -1
    daugiausia_tasku_vardas = ''

    for _ in range(n):
        eilute = failas.readline().split()

        mokinio_vardas = eilute[0]
        atliktu_uzd_skc = int(eilute[1])

        taskai = list(map(int,eilute[2:2 + atliktu_uzd_skc]))
        tasku_suma = sum(taskai)

        if daugiausia_tasku < tasku_suma:
            daugiausia_tasku = tasku_suma
            daugiausia_tasku_vardas = mokinio_vardas

        print(mokinio_vardas,atliktu_uzd_skc,tasku_suma)




print(f'Geriausias {daugiausia_tasku_vardas} {daugiausia_tasku}')

        
