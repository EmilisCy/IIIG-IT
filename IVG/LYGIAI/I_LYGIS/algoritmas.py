with open('IVG/LYGIAI/I_LYGIS/duomenys.txt', 'r') as failas:
    n = int(failas.readline())

    for _ in range(n):
        eilute = failas.readline().split()

        klases_pav = eilute[0]
        mokiniu_skc = int(eilute[1])

        pazymiu_eilute = failas.readline().split()

        pazymiai = list(map(int,pazymiu_eilute))
        pazymiu_suma = 0

        for pazymis in pazymiai:
            pazymiu_suma += pazymis


        print(klases_pav,pazymiu_suma)

