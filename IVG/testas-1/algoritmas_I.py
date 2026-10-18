taskai = []

with open('/Users/emiliscy/Desktop/IIIG-IT/IVG/testas-1/rezultatai_I.txt', 'r') as failas:
    n = int(failas.readline())

    geriausio_kodas = ''
    didziausia_suma = -1


    for _ in range(n):
        eilute = failas.readline().split()
        kodas = eilute[0]
        taskai = list(map(int, eilute[2:]))
        suma = sum(taskai)

        print(kodas,suma)

        if suma > didziausia_suma:
            didziausia_suma = suma
            geriausio_kodas = kodas

print(f'Geriausias: {geriausio_kodas} {didziausia_suma}')