def dazu_dezuciu_skaicius():
    with open('IIIG/Function-returning-calculated-value-threw-function-name/Dažytojas/duomenys4.txt', 'r') as f:
        dazu_dezutes_kaina_litrais = 0
        for line in f:
            x, y, a, l, k = map(float, line.split())
            dazu_dezutes_kaina_litrais += k
        
        paviršiaus_plotas = (x * a) + (y * a)
        dazu_skc_litrais = paviršiaus_plotas / l

    return dazu_skc_litrais, dazu_dezutes_kaina_litrais

def kaina_eurais(dazu_skc_litrais, dazu_dezutes_kaina_litrais):
    kaina = dazu_skc_litrais * dazu_dezutes_kaina_litrais
    kaina_eurais = kaina / 3.4528

    return round(kaina_eurais, 2)

dazu_dezuciu_skaicius, dazu_dezutes_kaina_litrais = dazu_dezuciu_skaicius()

kaina = kaina_eurais(dazu_dezuciu_skaicius, dazu_dezutes_kaina_litrais)

with open('IIIG/Function-returning-calculated-value-threw-function-name/Dažytojas/rezultatai4.txt', 'w') as e:
    e.write(f'{round(dazu_dezuciu_skaicius, 2)} {kaina}')

# rezultatai panasus bet nesigavo gauti vienodu