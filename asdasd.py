# Termékek listája: [Kód és név, Rendelt db, Ár]
from colorama import Fore, Style, init
import os
init(autoreset=True)
menu_elemek = [
    ["10) Borsodi", 0, 800], 
    ["11) TamasiHell", 0, 350],
    ["12) DobozosCola", 0, 600],
    ["13) CiganyViz", 0, 150],
    ["14) Fanta", 0, 600],
    ["30) Snikers", 0, 300],
    ["31) KinderRicardo", 0, 400],
    ["32) SportKocka", 0, 250],
    ["33) FeriCsoki", 0, 350],
    ["34) CsokiZotyaClaus", 0, 1000],
    ["35) CiniMinis", 0, 1000]
]

futas = True

while futas:
    # 1. Menü kiírása
    print("\n--- AUTOMATA MENÜ ---")
    for elem in menu_elemek:
        print(elem[0] + " - " + str(elem[2]) + " Ft")
    print("\n{Fore.Yellow} Q) Fizetés {Fore.reset}")
    
    valasz = input("\nMit szeretnél? (Adja meg a kódot, pl. 10): ").upper()

    # 2. Kilépés és fizetés
    if valasz == "Q":
        print("\n=== SZÁMLA ===")
        vegosszeg = 0
        
        # Számla kiszámolása
        for elem in menu_elemek:
            db = elem[1]
            ar = elem[2]
            if db > 0:
                reszosszeg = db * ar
                vegosszeg = vegosszeg + reszosszeg
                print(elem[0] + ": " + str(db) + " db = " + str(reszosszeg) + " Ft")
        
        print("Fizetendő összeg: " + str(vegosszeg) + " Ft")
        
        if vegosszeg > 0:
            # Pénz bedobása
            bedobva = 0
            while bedobva < vegosszeg:
                hiany = vegosszeg - bedobva
                print("Még hiányzik: " + str(hiany) + " Ft")
                bedobott = int(input("Dobj be pénzt (5, 10, 20, 50, 100, 200, 500, 1000...): "))
                bedobva = bedobva + bedobott
            
            # Visszajáró számolása
            visszajaro = bedobva - vegosszeg
            print("\nSikeres fizetés!")
            print("Visszajáró összeg: " + str(visszajaro) + " Ft")
            
            # Visszajáró címletezése
            if visszajaro > 0:
                print("Visszajáró érmékben/bankjegyekben:")
                cimletek = [20000, 10000, 5000, 2000, 1000, 500, 200, 100, 50, 20, 10, 5]
                for c in cimletek:
                    db_vissza = visszajaro // c
                    if db_vissza > 0:
                        print(str(c) + " Ft: " + str(db_vissza) + " db")
                        visszajaro = visszajaro % c
        
        print("\nKöszönjük a vásárlást!")
        futas = False  # Leállítja a ciklust

    # 3. Termék hozzáadása a kosárhoz
    else:
        db = int(input("Hány darabot kérsz?: "))
        talalt = False
        
        for elem in menu_elemek:
            if elem[0].startswith(valasz):
                elem[1] = elem[1] + db
                print("Hozzáadva!")
                talalt = True
                break
        
        if talalt == False:
            print("Nincs ilyen kódú termék!")