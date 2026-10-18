taskai = []

with open('/Users/emiliscy/Desktop/IIIG-IT/IVG/testas-1/rezultatai_II.txt', 'r') as failas:
    mokiniu_skaicius = int(failas.readline())

    geriausias_vardas = ''
    didziausia_suma = -1

    for _ in range(mokiniu_skaicius):
        vardas, veiklu_skaicius = failas.readline().split()
        veiklu_skaicius = int(veiklu_skaicius)

        bendra_suma = 0

        for _ in range(veiklu_skaicius):
            eilute = failas.readline().split()

            veiklos_kodas = eilute[0]
            dienu_skaicius = int(eilute[1])

            trukmes = list(map(int,eilute[2:]))
            bendra_suma += sum(trukmes)

        print(vardas,bendra_suma)

        if bendra_suma > didziausia_suma:
            didziausia_suma = bendra_suma
            geriausias_vardas = vardas

print(f'Geriausias: {geriausias_vardas} {didziausia_suma}')
            
        

