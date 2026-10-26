
def duomenu_nuskaitymas(kelias):
    with open(kelias, 'r', encoding='utf-8') as failas:
        eilute = failas.readline().split()

        n = int(eilute[0])
        k = int(eilute[1])

        dienos = list(map(int, failas.readline().split()))

    return n, k, dienos


def ilgiausia_seka(k, dienos):
    dabartine_seka = 0
    ilgiausia_seka = 0

    pradzia = 0
    geriausia_pradzia = 0
    geriausia_pabaiga = 0

    for numeris, aktyvumas in enumerate(dienos, start=1):
        if aktyvumas > k:
            if dabartine_seka == 0:
                pradzia = numeris

            dabartine_seka += 1

            if dabartine_seka > ilgiausia_seka:
                ilgiausia_seka = dabartine_seka
                geriausia_pradzia = pradzia
                geriausia_pabaiga = numeris
        else:
            dabartine_seka = 0

    if ilgiausia_seka == 0:
        return 0, 0, 0

    return ilgiausia_seka, geriausia_pradzia, geriausia_pabaiga


n, k, dienos = duomenu_nuskaitymas(
    'IVG/Darbas_su_nuskaitytais_duomenimis/III_užduotis/aktyvumas.txt'
)

ilgis, pradzia, pabaiga = ilgiausia_seka(k, dienos)

with open('Aktyvumas_rez.txt', 'w', encoding='utf-8') as failas:
    if ilgis == 0:
        failas.write('Aktyvių dienų nėra\n')
    else:
        failas.write(f'Ilgis {ilgis}\n')
        failas.write(f'Pradžia {pradzia}\n')
        failas.write(f'Pabaiga {pabaiga}\n')
