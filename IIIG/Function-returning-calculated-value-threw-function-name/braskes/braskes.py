def nuskaityti_duomenis():
    with open('IIIG/Function-returning-calculated-value-threw-function-name/braskes/duomenys5.txt', 'r') as f:
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