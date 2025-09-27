def nuskaityti_duomenis():
    with open('IIIG/Function-returning-calculated-value-threw-function-name/braskes/duomenys5.txt', 'r') as f:
        next(f)
        duomenys = [list(map(int, line.split())) for line in f]
        vardai = ['Vaida', 'Gytis', 'Jonas', 'Rasa']
    return vardai, duomenys

def braskiu_kiekis_kg(duomenys):
    braskiu_kiekis_sum = 0
    for line in duomenys:
        a, b, c, d = map(int, line)
        braskiu_kiekis_sum += a + b + c + d
            
    return braskiu_kiekis_sum

def daugiausiai_priskynusiu_vardai(vardai, duomenys):
    daugiausia_vardai = []
    vardai_braskiu_kiekis = {vardas: 0 for vardas in vardai}
    for i, kiekis in enumerate(line)
        vardai_braskiu_kiekis[vardai[i]] += kiekis

    max_kiekis = max(vardai_braskiu_kiekis.values())
    for vardas, kiekis in vardai_braskiu_kiekis.items():
        daugiausia_vardai(vardas)
    return daugiausia_vardai

with open('IIIG/Function-returning-calculated-value-threw-function-name/braskes/rezultatai5.txt') as e:
    e.write(f'')

