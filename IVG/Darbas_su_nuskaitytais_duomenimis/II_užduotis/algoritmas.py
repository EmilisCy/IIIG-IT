
def duomenu_nuskaitymas(kelias):
    with open(kelias, 'r', encoding='utf-8') as failas:
        eilute = failas.readline().split()

        n = int(eilute[0])
        r = int(eilute[1])

        dalyviai = []

        for _ in range(n):
            eilute = failas.readline().split()

            dalyvio_kodas = int(eilute[0])
            ivertinimai = list(map(int, eilute[1:]))

            dalyviai.append((dalyvio_kodas, ivertinimai))

    return n, r, dalyviai


def tasku_skaiciavimas(ivertinimai):
    return sum(ivertinimai)


def atitinka_salygas(r, ivertinimai):
    if 0 in ivertinimai:
        return False

    suma = tasku_skaiciavimas(ivertinimai)

    if suma >= r:
        return True

    return False


def atrinkti_dalyvius(r, dalyviai):
    atrinkti = []

    for kodas, ivertinimai in dalyviai:
        if atitinka_salygas(r, ivertinimai):
            suma = tasku_skaiciavimas(ivertinimai)
            atrinkti.append((kodas, suma))

    atrinkti.sort(key=lambda x: (-x[1], x[0]))

    return atrinkti


n, r, dalyviai = duomenu_nuskaitymas(
    'IVG/Darbas_su_nuskaitytais_duomenimis/II_užduotis/konkursas.txt'
)

atrinkti = atrinkti_dalyvius(r, dalyviai)

with open('Laikas_rez.txt', 'w', encoding='utf-8') as failas:
    if len(atrinkti) == 0:
        failas.write('Atrinktų dalyvių nėra')
    else:
        for kodas, suma in atrinkti:
            failas.write(f'{kodas} {suma}\n')
