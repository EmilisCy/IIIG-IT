
def duomenu_nuskaitymas(kelias):

    duomenys = []

    with open(kelias, 'r') as f:
        n = int(f.readline())

        for _ in range(n):
            eilute = f.readline().split()

            klases_kodas = eilute[0]
            mokiniu_skaicius = int(eilute[1])

            mokiniai = []

            for _ in range(mokiniu_skaicius):
                eilute = f.readline().split()

                vardas = eilute[0]
                konsultaciju_skaicius = int(eilute[1])
                laikas = list(map(int, eilute[2:2 + konsultaciju_skaicius]))

                mokiniai.append({
                    'vardas': vardas,
                    'konsultaciju_skaicius': konsultaciju_skaicius,
                    'laikas': laikas
                })

            duomenys.append({
                'klases_kodas': klases_kodas,
                'mokiniai': mokiniai
            })

    return duomenys


def konsultavimo_laikas(mokinys):

    suma = sum(mokinys['laikas'])

    return suma


def bendras_klases_laikas(klase):

    suma = 0

    for mokinys in klase['mokiniai']:
        suma += konsultavimo_laikas(mokinys)

    return suma


def didziausias_laikas_konsultacijose(mokiniai):

    didziausias_laikas = -1
    vardas = ''

    for mokinys in mokiniai:
        laikas = konsultavimo_laikas(mokinys)

        if laikas > didziausias_laikas:
            didziausias_laikas = laikas
            vardas = mokinys['vardas']

    return vardas, didziausias_laikas


def geriausia_komanda(duomenys):

    geriausia_komanda = ''
    geriausia_komanda_laikas = -1

    for klase in duomenys:
        suma = bendras_klases_laikas(klase)

        if suma > geriausia_komanda_laikas:
            geriausia_komanda_laikas = suma
            geriausia_komanda = klase['klases_kodas']

    return geriausia_komanda, geriausia_komanda_laikas



duomenys = duomenu_nuskaitymas('IVG/Bandomasis/V1_konsultacijos.txt')

for klase in duomenys:

    print('\nKlase:', klase['klases_kodas'])

    for m in klase['mokiniai']:
        suma = konsultavimo_laikas(m)
        print(m['vardas'], suma, 'min.')

    suma = bendras_klases_laikas(klase)
    print('Bendras klases laikas:', suma, 'min.')

    vardas, mokinio_laikas = didziausias_laikas_konsultacijose(klase['mokiniai'])
    print('Daugiausiai konsultavosi:', vardas, mokinio_laikas, 'min.')


kodas, bendras_laikas = geriausia_komanda(duomenys)

print('\nGeriausia klase:', kodas)
print('Bendras laikas:', bendras_laikas, 'min.')
