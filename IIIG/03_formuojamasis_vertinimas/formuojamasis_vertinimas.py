import os

KATALOGAS = os.path.dirname(os.path.abspath(__file__))
DUOMENYS = os.path.join(KATALOGAS, 'duomenys.txt')
REZULTATAI = os.path.join(KATALOGAS, 'rezultatai.txt')

def vidurkio_apskaiciavimas():
    pazymiai = []
    vidurkiai = []
    with open(DUOMENYS, 'r') as f:
        next(f)
        for line in f:
            p = list(map(int, line.split()))
            pazymiai.append(p)
    
    for p in pazymiai:
        if len(p) != 3:
            truksta = 3 - len(p)
            p.extend([0] * truksta)

        if all(x == 0 for x in p):
            vidurkis = 1
        else:
            p_be_nuliu = list(filter(lambda x: x != 0, p))
            if len(p_be_nuliu) > 0:
                vidurkis = sum(p_be_nuliu) / len(p_be_nuliu)
            else:
                vidurkis = int(sum(p) / len(p))

        if vidurkis % 1 > 0:
            vidurkis = int(vidurkis) + 1
        else:
            vidurkis = int(vidurkis)
        
        vidurkiai.append(vidurkis)

    
    with open(REZULTATAI, 'w') as e:
            e.write(', '.join(map(str, vidurkiai)))

vidurkio_apskaiciavimas()



           

#sitas uzdavinys yra visiskas vezys atrodo lengvas kol supranti kad nesupranti python visiskai!!!! taciau ismokau next() ir lamba su filter()
