with open('IVG/LYGIAI/III_LYGIS/duomenys.txt', 'r') as failas:
    n = int(failas.readline())

    geriausia_komanda = ''
    geriausios_komandos_taskai = -1

    for _ in range(n):
        eilute = failas.readline().split()

        komandos_pavadinimas = eilute[0]
        dalyviu_skaicius = int(eilute[1])

        pradiniai_komandu_taskai = 0
        geriausio_dalyvio_taskai = -1
        geriausias_vardas = ''

        for _ in range(dalyviu_skaicius):
            kita_eilute = failas.readline().split()

            dalyvio_vardas = kita_eilute[0]
            rungciu_taskai = list(map(int, kita_eilute[1:]))
            tasku_suma = sum(rungciu_taskai)

            pradiniai_komandu_taskai += tasku_suma

            if tasku_suma > geriausio_dalyvio_taskai:
                geriausio_dalyvio_taskai = tasku_suma
                geriausias_vardas = dalyvio_vardas

        print(f'{komandos_pavadinimas} {pradiniai_komandu_taskai} Geriausias: {geriausias_vardas} {geriausio_dalyvio_taskai}')

        if pradiniai_komandu_taskai > geriausios_komandos_taskai:
            geriausios_komandos_taskai = pradiniai_komandu_taskai
            geriausia_komanda = komandos_pavadinimas

    print(f'Geriausia komanda: {geriausia_komanda} {geriausios_komandos_taskai}')