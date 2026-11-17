
def nuskaitimas(kelias):
    with open(kelias, 'r') as failas:
        irasu_skaicius = int(failas.readline())

        duomenys = []

        for _ in range(irasu_skaicius):
            eilute = failas.readline().strip().split(';')

            knygos_kodas = eilute[0]
            kategorija = eilute[1]
            isleidimo_metai = int(eilute[2])
            puslapiu_skaicius = int(eilute[3])
            skaitytoju_ivertinimas = float(eilute[4])

            duomenys.append({
                'knygos_kodas': knygos_kodas,
                'kategorija': kategorija,
                'isleidimo_metai': isleidimo_metai,
                'puslapiu_skaicius': puslapiu_skaicius,
                'skaitytoju_ivertinimas': skaitytoju_ivertinimas
            })

        metai_reikalavimas, ivertinimas_reikalavimas = failas.readline().split()

        metai_reikalavimas = int(metai_reikalavimas)
        ivertinimas_reikalavimas = float(ivertinimas_reikalavimas)

    return duomenys, metai_reikalavimas, ivertinimas_reikalavimas


def knygu_atrikiavimas(duomenys, metai_reikalavimas, ivertinimas_reikalavimas):
    tinkamos_knygos = []

    for knyga in duomenys:
        if (knyga['skaitytoju_ivertinimas'] >= ivertinimas_reikalavimas
                and knyga['isleidimo_metai'] >= metai_reikalavimas):
            tinkamos_knygos.append(knyga)

    return tinkamos_knygos


def knygu_rusiavimas(tinkamos_knygos):
    tinkamos_knygos.sort(
        key=lambda knyga: (
            -knyga['skaitytoju_ivertinimas'],
            -knyga['isleidimo_metai'],
            knyga['knygos_kodas']
        )
    )

    return tinkamos_knygos


def knygos_pagal_kategorija(tinkamos_knygos):
    kategorijos = {}

    for knyga in tinkamos_knygos:
        kategorija = knyga['kategorija']

        if kategorija not in kategorijos:
            kategorijos[kategorija] = 0

        kategorijos[kategorija] += 1

    return kategorijos


def rezultatu_isvedimas(tinkamos_knygos):
    if len(tinkamos_knygos) == 0:
        print("Atrinktų įrašų nėra")

    else:
        for knyga in tinkamos_knygos:
            print(
                knyga['knygos_kodas'],
                knyga['kategorija'],
                knyga['isleidimo_metai'],
                knyga['puslapiu_skaicius'],
                f"{knyga['skaitytoju_ivertinimas']:g}"
            )

        print("\nKnygų skaičius pagal kategorijas:")

        kategorijos = knygos_pagal_kategorija(tinkamos_knygos)

        for kategorija, kiekis in kategorijos.items():
            print(kategorija, kiekis)

duomenys, metai_reikalavimas, ivertinimas_reikalavimas = nuskaitimas(
    'IVG/Bandomasis/V2/ANTRAS_PROGRAMAVIMO_UZD/V2_knygos.txt'
)

tinkamos_knygos = knygu_atrikiavimas(
    duomenys,
    metai_reikalavimas,
    ivertinimas_reikalavimas
)

rusiuotos_knygos = knygu_rusiavimas(tinkamos_knygos)

rezultatu_isvedimas(rusiuotos_knygos)
