import os

KATALOGAS = os.path.dirname(os.path.abspath(__file__))
DUOMENYS = os.path.join(KATALOGAS, 'duomenys.txt')
REZULTATAI = os.path.join(KATALOGAS, 'rezultatai.txt')

def nuskaityti_duomenis():
    with open(DUOMENYS, 'r') as f:
        next(f)
        duomenys = [list(map(int, line.split())) for line in f]
    vardai = ['Vaida', 'Gytis', 'Jonas', 'Rasa']
    eiluciu_skaicius = len(duomenys)

    return vardai, duomenys, eiluciu_skaicius

def braskiu_kiekis_kg(duomenys):
    braskiu_kiekis_sum = 0
    for line in duomenys:
        a, b, c, d = map(int, line)
        braskiu_kiekis_sum += a + b + c + d
            
    return braskiu_kiekis_sum

def daugiausiai_per_diena(vardai, duomenys):
    rezultatai = []
    for diena, eilute in enumerate(duomenys, start=1):
        max_kiekis = max(eilute)

        daugiausiai_vardai = []
        for i, kiekis in enumerate(eilute):
            if kiekis == max_kiekis:
                daugiausiai_vardai.append(vardai[i])


vardai, duomenys, eiluciu_skaicius = nuskaityti_duomenis()

#nebegaliu mission failed