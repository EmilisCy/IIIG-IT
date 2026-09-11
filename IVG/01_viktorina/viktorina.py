import os

KATALOGAS = os.path.dirname(os.path.abspath(__file__))
DUOMENYS = os.path.join(KATALOGAS, 'duomenys.txt')
REZULTATAI = os.path.join(KATALOGAS, 'rezultatai.txt')

def statistika(komandos,pavadinimai,laikai):
    for i in range(len(pavadinimai)):
        rasta = False
        for komanda in komandos:
            if komanda[0] == pavadinimai[i]:
                komanda[1]+=1
                komanda[2]+=laikai[1]
                rasta = True
                break
        if not rasta:
            komandos.append([pavadinimai[i],laikai[i]])

with open(DUOMENYS) as duomenys:
    k = int(duomenys.readline())
    komandos =[]
    didziausias_laikas = -1
    sunkus_klausimai = []

    for _ in range(k):
        eilute = duomenys.readline().split()
        klausimo_numeris = eilute[0]
        komandu_skaicius = int(eilute[1])


        pavadinimai = []
        laikai = []
        pozicija = 2
        for _ in range(komandu_skaicius):
            komandos_pavadinimas = eilute[pozicija]
            laikas = float(eilute[pozicija+1])
            pavadinimai.append(komandos_pavadinimas)
            laikai.append(laikas)

            if laikas>didziausias_laikas:
                didziausias_laikas = laikas
                sunkus_klausimai = [klausimo_numeris]
            elif laikas == didziausias_laikas:
                sunkus_klausimai.append(klausimo_numeris)
            pozicija += 2

        statistika(komandos,pavadinimai,laikai)

komandos.sort(key =lambda komanda: (-komanda[1],komanda[2]))

with open(REZULTATAI, 'w') as rezultatai:
    rezultatai.write(f'{didziausias_laikas}\n')
    rezultatai.write(f'{sunkus_klausimai}\n')
    for komanda in komandos:
        rezultatai.write(
            f"{komanda[0]}"\n
            f"{komanda[1]}"\n
            f"{komanda[2]}"\n
        )
