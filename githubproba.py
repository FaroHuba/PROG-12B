szamok=[]
for i in range(5):
    szamok.append(int(input("Adj meg egy szamot:")))
osszeg=0
for szam in szamok:
    osszeg+=szam
print(f"Átlag: {osszeg/len(szamok)}")

#van e paros szam
i=0
while i < len(szamok) and szamok[i] % 2!=0:
    i+=1
if i<len(szamok):
    print("Van páros szám")
else:
    print("Nincs paros szam")
