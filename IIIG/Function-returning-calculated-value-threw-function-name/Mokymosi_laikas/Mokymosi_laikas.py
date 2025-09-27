# def apskaiciuoti_mokymosi_laika():
#     with open('IIIG/Function-returning-calculated-value-threw-function-name/Mokymosi_laikas/duomenys2.txt', 'r') as f:
#        bendras_laikas = 0
#        for line in f.readlines()[1:]:
#             h1, m1, h2, m2 = map(int, line.split())
#             pradinis = h1 * 60 + m1
#             galinis = h2 * 60 + m2
#             bendras_laikas += galinis - pradinis     

#     with open('IIIG/Function-returning-calculated-value-threw-function-name/Mokymosi_laikas/rezultatai2.txt', 'w') as e:
#         valandos = bendras_laikas // 60
#         minutes = bendras_laikas % 60
#         e.write(f'{valandos} val. {minutes} min.')

# apskaiciuoti_mokymosi_laika()

#sis budas atrodo labai vaikiskas todel bandysiu daryti su dic ir enumerate

def apskaiciuoti_mokymosi_laika():
    mokymosi_laikai = {}
    with open('IIIG/Function-returning-calculated-value-threw-function-name/Mokymosi_laikas/duomenys2.txt', 'r') as f:
        bendras_laikas = 0
        for index, line in enumerate(f.readlines()[1:], start=1):
            h1, m1, h2, m2 = map(int, line.split())
            pradinis = h1 * 60 + m1
            galinis = h2 * 60 + m2
            trukme = galinis - pradinis
            bendras_laikas += trukme

            mokymosi_laikai[index] = {'pradinis': (h1, m1), 'galinis': (h2, m2), 'trukme': trukme}

    with open('IIIG/Function-returning-calculated-value-threw-function-name/Mokymosi_laikas/rezultatai2.txt', 'w') as e:
        valandos = bendras_laikas // 60
        minutes = bendras_laikas % 60
        e.write(f'{valandos} val. {minutes} min.\n')

        for index, data in mokymosi_laikai.items():
            e.write(f"Intervalas {index},  pradinis laikas: {data['pradinis'][0]}:{data['pradinis'][1]}, galinis laikas {data['galinis'][0]}:{data['galinis'][1]},  trukme: {data['trukme']} minutes \n")

apskaiciuoti_mokymosi_laika()