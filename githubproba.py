szamok=[]
for i in range(5):
    szamok.append(int(input("Adj meg egy szamot:")))
osszeg=0
for szam in szamok:
    osszeg+=szam
print(f"Átlag: {osszeg/len(szamok)}")