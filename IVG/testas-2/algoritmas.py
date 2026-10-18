with open('/Users/emiliscy/Desktop/IIIG-IT/IVG/testas-2/temperaturos.txt', 'r') as failas:
    n = int(failas.readline())

    for _ in range(n):
        eilute = failas.readline().split()

        stoties_kodas = eilute[0]
        matavimu_skaicius = int(eilute[1])

        temperaturos = list(map(float, eilute[2:2 + matavimu_skaicius]))

        pradine_temperatura = 0
        auksciausia_temp = 0
        auksciausia_temp_miestas = ''

        for temp in temperaturos:
            pradine_temperatura += temp

            if auksciausia_temp < temp:
                auksciausia_temp = temp
                auksciausia_temp_miestas = stoties_kodas



        vidutine_temp = round(pradine_temperatura/matavimu_skaicius,1)



        print(stoties_kodas,vidutine_temp)

print(f'Aukščiausia temperatūra: {auksciausia_temp_miestas} {auksciausia_temp}')




            
