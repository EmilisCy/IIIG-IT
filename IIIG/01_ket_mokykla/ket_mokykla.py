import os

KATALOGAS = os.path.dirname(os.path.abspath(__file__))
DUOMENYS = os.path.join(KATALOGAS, 'duomenys.txt')
REZULTATAI = os.path.join(KATALOGAS, 'rezultatai.txt')

def vairavimo_mokyklos_geriausi_pazymiai():
    rezultatai = []
    geriausi_rezultatai = []
    with open(DUOMENYS, 'r') as f:
        n = int(f.readline().strip())
        for line in f:
            rezultatai.append(list(map(int, line.split()))) 
    for rezultatas in rezultatai:
        geriausi_rezultatai.append(max(rezultatas))

    with open(REZULTATAI, 'w') as e:
        for reiksme in geriausi_rezultatai:
            e.write(f'{reiksme}\n')

vairavimo_mokyklos_geriausi_pazymiai()