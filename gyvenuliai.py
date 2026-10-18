
# duomenys = []

# with open('duomenys.csv', 'r') as failas:
#     for eilute in failas:
#         eilute = eilute.strip()
#         laukai = eilute.split(';')

#         duomenys.append({
#             'savivaldybe': laukai[0].strip(),
#             'seniunija':   laukai[1].strip(),
#             'vietove':     laukai[2].strip(),
#             'gatve':       laukai[3].strip(),
#             'rusis':       laukai[4].strip(),
#             'skaicius':    int(laukai[5]),
#         }
#         )
# bendras_skaicius = 0
# for gyvenulis in duomenys:
#     bendras_skaicius += gyvenulis['skaicius']


# rusiu_skaiciai = {}
# for gyvenulis in duomenys:
#     rusis = gyvenulis['rusis']
#     if rusis not in rusiu_skaiciai:      
#         rusiu_skaiciai[rusis] = 0       
#     rusiu_skaiciai[rusis] += gyvenulis['skaicius']


# savivaldybes = {}

# for gyvunelis in duomenys:

#     savivaldybe = gyvunelis['savivaldybe']
#     rusis = gyvunelis['rusis']
#     skaicius = gyvunelis['skaicius']

#     if savivaldybe not in savivaldybes:
#         savivaldybes[savivaldybe] = {}

#     if rusis not in savivaldybes[savivaldybe]:
#         savivaldybes[savivaldybe][rusis] = 0

#     savivaldybes[savivaldybe][rusis] += skaicius
#     savivaldybes[savivaldybe].sort()




# with open('rezultatai.txt', 'w') as failas:

#     failas.write(bendras_skaicius)


# duomenys = []

# with open('/Users/emiliscy/Desktop/IIIG-IT/gyvenuliai.py', 'r') as failas:
#     n = int(failas.readline())
#     for _ in range(n):
#         eilute = failas.readline().strip().split()

#         pamoka = eilute[0]
#         laikas = eilute[1:]

#         duomenys.append({
#             'komanda': pamoka,
#             'laikas': laikas
#         })



 