
def vairavimo_mokyklos_geriausi_pazymiai():
    rezultatai = []
    geriausi_rezultatai = []
    with open('IIIG/Function-returning-calculated-value-threw-function-name/KET_Mokykla/duomenys1.txt', 'r') as f:
        n = int(f.readline().strip())
        for line in f:
            rezultatai.append(list(map(int, line.split()))) 
    for rezultatas in rezultatai:
        geriausi_rezultatai.append(max(rezultatas))

    with open('IIIG/Function-returning-calculated-value-threw-function-name/KET_Mokykla/rezultatas1.txt', 'w') as e:
        for reiksme in geriausi_rezultatai:
            e.write(f'{reiksme}\n')

vairavimo_mokyklos_geriausi_pazymiai()