def nuskaitymas(kelias):

    komandos = []

    with open(kelias, 'r') as failas:
        komandu_skaicius = int(failas.readline())

        for _ in range(komandu_skaicius):
            eilute = failas.readline().split()

            komandos_pavadinimas = eilute[0]
            skaitytoju_skaicius = int(eilute[1])

            skaitytojai = []

            for _ in range(skaitytoju_skaicius):
                eilute = failas.readline().split()

                vardas = eilute[0]
                savaiciu_skaicius = int(eilute[1])
                perskaitytu_psl_skc = list(map(int, eilute[2:2+savaiciu_skaicius]))

                skaitytojai.append({
                    'vardas': vardas,
                    'savaiciu_skc': savaiciu_skaicius,
                    'perskaitytu_psl_skc': perskaitytu_psl_skc
                })

            komandos.append({
                'komandos_pavadinimas': komandos_pavadinimas,
                'skaitytoju_skc': skaitytoju_skaicius,
                'skaitytojai': skaitytojai
            })

    return komandos


komandos = nuskaitymas('IVG/Bandomasis/V2/V2_skaitymas.txt')


def skaitytojo_puslapio_suma(skaitytojas):
    suma = 0

    for puslapiai in skaitytojas['perskaitytu_psl_skc']:
        suma += puslapiai

    return suma

def komandos_puslapiu_suma(komanda):
    suma = 0

    for skaitytojas in komanda["skaitytojai"]:
        suma += skaitytojo_puslapio_suma(skaitytojas)

    return suma

def daugiausiai_komandoje_perskaites(skaitytojai):
    vardas = ''
    daugiausiai_perskaityta = -1

    for skaitytojas in skaitytojai:
        skaicius = skaitytojo_puslapio_suma(skaitytojas)
        if daugiausiai_perskaityta < skaicius:
            daugiausiai_perskaityta= skaicius
            vardas = skaitytojas['vardas']

    return daugiausiai_perskaityta, vardas

def geriausia_komanda(komandos):
    geriausia_komanda = ''
    puslapiu_skaicius = -1

    for komanda in komandos:
        suma = komandos_puslapiu_suma(komanda)

        if suma > puslapiu_skaicius:
            geriausia_komanda = komanda['komandos_pavadinimas']
            puslapiu_skaicius = suma

    return geriausia_komanda, puslapiu_skaicius

for komanda in komandos:
    print('\nKomanda',komanda['komandos_pavadinimas'])
    for skaitytojas in komanda['skaitytojai']:
        suma = skaitytojo_puslapio_suma(skaitytojas)
        print(skaitytojas['vardas'], suma ,'puslapių')


    suma = komandos_puslapiu_suma(komanda)
    print("Bendras komandos perskaitytų puslapių skč:" ,suma)

    daugiausia_perskaityta, vardas = daugiausiai_komandoje_perskaites(komanda["skaitytojai"])
    print('Daugiausiai perskaitė:', vardas, daugiausia_perskaityta)

geriausia_komanda, puslapiu_skaicius = geriausia_komanda(komandos)

print('\nDaugiausia perskaičiusi komanda:', geriausia_komanda)
print('\nPerskaitytas puslapių skaičius', puslapiu_skaicius)