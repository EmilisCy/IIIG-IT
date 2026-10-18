with open('IVG/LYGIAI/IV_LYGIS/duomenys.txt', 'r') as failas:
    n = int(failas.readline())

    daugiausia_sunaudojo = ''
    daugiausia_sunaudojo_suma = -1

    for _ in range(n):
        eilute = failas.readline().split()

        pastato_kodas = eilute[0]
        menesiu_skaicius = int(eilute[1])

        bendra_suma = 0
        didziausias_menuo = -1
        didziausias_menuo_pavadinimas = ''

        print(pastato_kodas)

        for _ in range(menesiu_skaicius):
            duomenu_eilute = failas.readline().split()

            menesio_pavadinimas = duomenu_eilute[0]
            matavimu_skaicius = int(duomenu_eilute[1])
            suvartojimu_skaicius = list(map(int, duomenu_eilute[2:2 + matavimu_skaicius]))

            menesio_suma = sum(suvartojimu_skaicius)
            bendra_suma += menesio_suma

            if menesio_suma > didziausias_menuo:
                didziausias_menuo = menesio_suma
                didziausias_menuo_pavadinimas = menesio_pavadinimas

            print(menesio_pavadinimas, menesio_suma)

        print(f'Iš viso: {bendra_suma}')
        print(f'Didžiausia suma: {didziausias_menuo_pavadinimas} {didziausias_menuo}')

        if bendra_suma > daugiausia_sunaudojo_suma:
            daugiausia_sunaudojo_suma = bendra_suma
            daugiausia_sunaudojo = pastato_kodas

    print(f'Daugiausia sunaudojo: {daugiausia_sunaudojo} {daugiausia_sunaudojo_suma}')