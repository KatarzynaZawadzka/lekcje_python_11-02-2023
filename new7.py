with open('myfile.txt', 'r') as plik_txt:
    cala_tresc = plik_txt.read()

def ile_slow (tekst):
    podzielonytekst = tekst.split()
    return len(set(podzielonytekst))

print(cala_tresc)
cala_tresc = cala_tresc.split()
print('tekst', cala_tresc)

for i in range(len(cala_tresc)):
    cala_tresc[i] = cala_tresc[i].upper().replace(',','')

print('tekst slowo', cala_tresc)

print('listas', len(set(cala_tresc)))