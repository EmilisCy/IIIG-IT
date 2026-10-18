with open('IVG/LYGIAI/V_LYGIS/duomenys.txt', 'r') as failas:
    mokyklu_skaicius = int(failas.readline())

    geriausia_mokykla = ''
    geriausia_mokykla_taskai = -1
    minimalus_reikalavimas = 0


    for _ in range(mokyklu_skaicius):
        mokyklos_eilute = failas.readline().split()

        mokyklos_kodas = mokyklos_eilute[0]
        komandu_skaicius = int(mokyklos_eilute[1])

        mokyklos_tasku_suma = 0
        geriausia_komanda = ''
        geriausia_komanda_taskai = -1


        print(mokyklos_kodas)

        for _ in range(komandu_skaicius):
            komandos_eilute = failas.readline().split()

            komandos_pavadinimas = komandos_eilute[0]
            mokiniu_skaicius = int(komandos_eilute[1])

            komandu_tasku_suma = 0
            geriausias_mokinys = ''
            geriausio_mokinio_taskai = -1


            for _ in range(mokiniu_skaicius):
                mokinio_eilute = failas.readline().split()

                vardas = mokinio_eilute[0]
                atliktu_uzduociu_skaicius = int(mokinio_eilute[1])
                taskai = list(map(int,mokinio_eilute[2: 2 + atliktu_uzduociu_skaicius]))

                komandu_tasku_suma += sum(taskai)

                if sum(taskai) > geriausio_mokinio_taskai:
                    geriausio_mokinio_taskai = sum(taskai)
                    geriausias_mokinys = vardas

                if sum(taskai) >= 25:
                    minimalus_reikalavimas +=1


            mokyklos_tasku_suma += komandu_tasku_suma

            if geriausia_komanda_taskai < komandu_tasku_suma:
                geriausia_komanda_taskai = komandu_tasku_suma
                geriausia_komanda = komandos_pavadinimas

                
            print(f'{komandos_pavadinimas} {komandu_tasku_suma} Geriausias mokinys: {geriausias_mokinys} {geriausio_mokinio_taskai}')

        print(f'Mokyklos suma: {mokyklos_tasku_suma}')

        print(f'Geriausia komanda: {geriausia_komanda} {geriausia_komanda_taskai}')

        if geriausia_mokykla_taskai < mokyklos_tasku_suma:
            geriausia_mokykla_taskai = mokyklos_tasku_suma
            geriausia_mokykla = mokyklos_kodas

    print(f'Geriausia mokykla: {geriausia_mokykla} {geriausia_mokykla_taskai}')
    print(f'Bent 25 taškus surinko: {minimalus_reikalavimas}')
    

