# duomenys = []

# with open('Praktika/duomenys1.txt', 'r') as failas:
#     n = int(failas.readline().replace('\u200b', ''))

#     for _ in range(n):
#         eilute = failas.readline().strip()

#         while not eilute:
#             eilute = failas.readline().strip()

#         eilute = eilute.replace('\u200b', '').split()

#         kodas = eilute[0]
#         taskai = list(map(int,eilute[1:]))

#         duomenys.append({
#             'kodas': kodas,
#             'taskai': taskai
#         })

# def dalyviu_balu_sumavimas(duomenys):
#     rezultatai = []
#     for duomuo in duomenys:
#         kodas = duomuo['kodas']
#         balai = duomuo['taskai']
#         suma = sum(balai)
#         rezultatai.append((kodas,suma))

#     return rezultatai

# rezultatai = dalyviu_balu_sumavimas(duomenys)
# print(rezultatai)

# for kodas, suma in rezultatai:
#     print(kodas,suma)

# def grazinti_didziausia_reiksme(rezultatai):
#     didziausias = rezultatai[0]
#     for rezultatas in rezultatai:
#         if rezultatas[1] > didziausias[1]:
#             didziausias = rezultatas

#         return [didziausias]

# didziausias = grazinti_didziausia_reiksme(rezultatai)
# for rezultatas in didziausias:
#     print(rezultatas[0],rezultatas[1])

# # [('kodas','balas')]
    
with open('/Users/emiliscy/Desktop/IIIG-IT/Praktika/duomenys1.txt', 'r') as failas:
    k = int(failas.readline())

    laimejimai = {}
    komandu_eile = []

    for _ in range(k):
        eilute = failas.readline().split()
        klausimo_id = eilute[0]
        komandu_skaicius = int(eilute[1])

        pozicija = 2
        greiciausias_laikas = float('inf')
        greiciausia_komanda = ''

        for _ in range(komandu_skaicius):
            komanda = eilute[pozicija]
            laikas = float(eilute[pozicija + 1])

            if komanda not in laimejimai:
                laimejimai[komanda] = 0
                komandu_eile.append(komanda)

            if laikas < greiciausias_laikas:
                greiciausias_laikas = laikas
                greiciausia_komanda = komanda

            pozicija += 2

        laimejimai[greiciausia_komanda] += 1

        print(klausimo_id,
              greiciausia_komanda,
              greiciausias_laikas,
              komandu_eile,
              laimejimai)

dazniausiai_laimejo = komandu_eile[0]

for komanda in komandu_eile:
    if laimejimai[komanda] > laimejimai[dazniausiai_laimejo]:
        dazniausiai_laimejo = komanda

print(
    "Dažniausiai laimėjo:",
    dazniausiai_laimejo,
    laimejimai[dazniausiai_laimejo]
)


# Kiekvienam klausimui randa mažiausią laiką pasiekusią komandą. 
# K1 4 Alfa 6.8 Beta 7.2 Gama 5.9 Delta 6.1 
# Išveda klausimo ID, komandos pavadinimą ir laiką. 


