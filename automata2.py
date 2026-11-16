# GLOBÁLIS VÁLTOZÓK
# [Termék kódja és neve, Rendelt darabszám, Egységár]
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

# 1. Menü kiíratása
def menu_kiiras():
    print("\n--- ÉTEL- ÉS ITALAUTOMATA ---")
    for elem in menu_elemek:
        print(elem[0] + " - " + str(elem[2]) + " Ft")
    print("Q) Fizetés és Kilépés")
    print("----------------------------")

# 2. Rendelés hozzáadása
def rendeles(kod, darab):
    talalt = False
    for elem in menu_elemek:
        # Megnézzük, hogy a termék kódjával kezdődik-e a menüpont
        if elem[0].startswith(kod):
            elem[1] = elem[1] + darab
            print("Hozzáadva a kosárhoz: " + str(darab) + " db " + elem[0])
            talalt = True
            break
    
    if talalt == False:
        print("Nincs ilyen kódú termék!")

# 3. Címletezés (Visszajáró kiszámolása)
def cimletezes(visszajaro):
    print("\nVisszajáró címletezve:")
    cimletek = [20000, 10000, 5000, 2000, 1000, 500, 200, 100, 50, 20, 10, 5]
    
    for c in cimletek:
        db = visszajaro // c  # Egész osztással megkapjuk hány darab kell
        if db > 0:
            print(str(c) + " Ft-osból: " + str(db) + " db")
            visszajaro = visszajaro % c  # A maradék összeget visszük tovább

# 4. Fizetés és számla
def fizetes():
    print("\n====================")
    print("      SZÁMLA        ")
    print("====================")
    
    vegosszeg = 0
    for elem in menu_elemek:
        db = elem[1]
        ar = elem[2]
        if db > 0:
            reszösszeg = db * ar
            vegosszeg = vegosszeg + reszösszeg
            print(elem[0] + ": " + str(db) + " db x " + str(ar) + " Ft = " + str(reszösszeg) + " Ft")
    
    print("--------------------")
    print("Fizetendő összeg: " + str(vegosszeg) + " Ft")
    print("--------------------")

    if vegosszeg == 0:
        print("Nem vásároltál semmit!")
        return

    # Pénz bedobása
    bedobva = 0
    elfogadott_penzek = [5, 10, 20, 50, 100, 200, 500, 1000, 2000, 5000, 10000, 20000]

    while bedobva < vegosszeg:
        hiany = vegosszeg - bedobva
        print("Még hiányzik: " + str(hiany) + " Ft")
        bedobott_penz = int(input("Dobj be egy érmét vagy bankjegyet: "))

        if bedobott_penz in elfogadott_penzek:
            bedobva = bedobva + bedobott_penz
        else:
            print("Ilyen érmét/bankjegyet nem fogad el az automata!")

    # Visszajáró kezelése
    visszajaro = bedobva - vegosszeg
    print("\nSikeres fizetés!")
    print("Bedobott pénz: " + str(bedobva) + " Ft")
    print("Visszajáró: " + str(visszajaro) + " Ft")

    if visszajaro > 0:
        cimletezes(visszajaro)
    else:
        print("Pontos összeget adtál meg, nincs visszajáró.")

# --- FŐPROGRAM ---
futar = True

while futar:
    menu_kiiras()
    valasztas = input("Válassz terméket (adja meg a kódot, pl. 10) vagy 'Q' a fizetéshez: ").upper()

    if valasztas == "Q":
        fizetes()
        futar = False  # Kilépünk a ciklusból
    else:
        db = int(input("Hány darabot kérsz?: "))
        if db > 0:
            rendeles(valasztas, db)
        else:
            print("A darabszámnak pozitívnak kell lennie!")