def duomenu_nuskaitymas(kelias):
    with open(kelias, 'r', encoding='utf-8') as failas:
        n = int(failas.readline())

        turima = []
        pokytis = []

        for _ in range(n):
            eilute = failas.readline().strip().split()
            pavadinimas = ' '.join(eilute[:2])
            kiekis = int(eilute[2])

            turima.append((pavadinimas,kiekis))

        k = int(failas.readline())



        for _ in range(k):
            eilute = failas.readline().strip().split()

            detales_numeris = int(eilute[0])
            kiekio_pokytis = int(eilute[1])

            pokytis.append((detales_numeris,kiekio_pokytis))

            


    return turima, pokytis


turima, pokytis = duomenu_nuskaitymas('IVG/Klases_darbas/auto/duomenys.txt')

print(turima, pokytis)