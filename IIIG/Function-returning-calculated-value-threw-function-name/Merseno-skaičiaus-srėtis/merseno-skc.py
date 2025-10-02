#Sukuriame bendra masyva
bendras_masyvas = list(range(1, 10001))

#Funkcija kuri paiima vartotojo duomenis
def nuskaitome_duomenis():
    vartotojo_duomenys = []
    with open('IIIG/Function-returning-calculated-value-threw-function-name/Merseno-skaičiaus-srėtis/duomenys6.txt', 'r') as f:
        for domuo in f:
            vartotojo_skc = map(int, domuo.split())
            vartotojo_duomenys.extend(vartotojo_skc)
    return vartotojo_duomenys

#Surandame visus pirminius skc is bendro masyvo
def yra_pirminis(bendras_masyvas):
    pirminiai_skc = []
    for skaicius in bendras_masyvas:
        if skaicius == 0 or skaicius == 1:
            continue

        yra_pirminis = True
        for i in range(2, skaicius):
            if skaicius % i == 0:
                yra_pirminis = False
                break

        if yra_pirminis:
            pirminiai_skc.append(skaicius)

    return pirminiai_skc

# #Surandame visus merseno skc is pirminiu masyvo
def yra_merseno_skc(bendras_masyvas, pirminiai_skc):
    merseno_skc = []
    for n in pirminiai_skc:
        merseno_skaicius = 2**n - 1
        if yra_pirminis([merseno_skaicius]):
            merseno_skc.append(merseno_skaicius)

    return merseno_skc


#surandame visus merseno skaicius is vartotojo duoto intervalo

def mersenas_data_int(vartotojo_duomenys, merseno_skc):
    grazinimo_duomenis = []

    a = vartotojo_duomenys[0]
    b = vartotojo_duomenys[1]
    
    duotu_duomenu_int = list(range(a, (b + 1)))

    for merseno_skaicius in merseno_skc:
        if merseno_skaicius in duotu_duomenu_int:
            grazinimo_duomenis.append(merseno_skaicius)

    return grazinimo_duomenis

#sulinkiname funkcijas
start_time = time.time()

vartotojo_duomenys = nuskaitome_duomenis()

pirminiai_skc = yra_pirminis(bendras_masyvas)

merseno_skc = yra_merseno_skc(bendras_masyvas, pirminiai_skc)

grazinimo_duomenis = mersenas_data_int(vartotojo_duomenys, merseno_skc)

#irasome rezultatus i rezultatas6.txt


with open('IIIG/Function-returning-calculated-value-threw-function-name/Merseno-skaičiaus-srėtis/rezultatas6.txt', 'w') as e:
    e.write(" ".join(map(str, grazinimo_duomenis)))
    
end_time = time.time()
print(f"Programa užtruko {end_time - start_time} sekundes.")