def nuskaityti_duomenis(kelias):
    with open(kelias, 'r', encoding='utf-8') as failas:
        dienu_skc = int(failas.readline())
        laikai = list(map(int, failas.readline().split()))

    return laikai


def bendras_laikas(laikai):
    return sum(laikai)


def vidurkis(laikai):
    return sum(laikai) / len(laikai)


def didziausias_laikas_ir_diena(laikai):
    didziausias = max(laikai)
    return didziausias, laikai.index(didziausias) + 1


def virs_vidurkio(laikai):
    virs_vidurkio = 0
    vid = vidurkis(laikai)

    for laikas in laikai:
        if laikas > vid:
            virs_vidurkio += 1

    return virs_vidurkio


laikai = nuskaityti_duomenis('IVG/Darbas_su_nuskaitytais_duomenimis/I_užduotis/laikas.txt')

didziausias, diena = didziausias_laikas_ir_diena(laikai)

with open('Laikas_rez.txt', 'w', encoding='utf-8') as failas:
    failas.write(f'Iš viso {bendras_laikas(laikai)}\n')
    failas.write(f'Vidurkis {vidurkis(laikai):.2f}\n')
    failas.write(f'Didžiausia trukmė {didziausias}\n')
    failas.write(f'Diena {diena}\n')
    failas.write(f'Virš vidurkio {virs_vidurkio(laikai)}\n')
