# IMPORT
from colorama import Fore, Style, init
import os

# Colorama inicializálása
init(autoreset=True)

# GLOBÁLIS VÁLTOZÓK
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
    ["35) CiniMinis", 0, 1000],
    ["Q) Fizetés és Kilépés", 0, 0]
]   

# FÜGGVÉNY DEFINÍCIÓK
def kepernyo_torles():
    os.system('cls' if os.name == 'nt' else 'clear')

def menu():
    kepernyo_torles()
    print(f"{Fore.RED}=== ÉTEL- ÉS ITALAUTOMATA ==={Fore.RESET}")
    print(f"{'=' * 40}")
    
    for m in menu_elemek:
        if m[0].startswith('Q'):
            print(f"{Fore.YELLOW}{m[0]}{Fore.RESET}")
        else:
            print(f"{m[0]:25} {m[2]:>6} Ft")
    print(f"{'=' * 40}\n")

def rendeles(kod, db):
    talalat = False
    for item in menu_elemek:
        if item[0].startswith(kod):
            item[1] += db
            print(f"\n{Fore.GREEN}Hozzáadva: {db} db - {item[0][4:]}{Fore.RESET}")
            talalat = True
            break
    
    if not talalat:
        print(f"\n{Fore.RED}Érvénytelen termékkód!{Fore.RESET}")

def cimletezes(osszeg):
    """Kiszámolja, hogy hány darab érmére/bankjegyre van szükség a visszajáróhoz."""
    # A legnagyobbtól a legkisebb címletig haladunk
    cimletek = [20000, 10000, 5000, 2000, 1000, 500, 200, 100, 50, 20, 10, 5]
    
    print(f"\n{Fore.CYAN}Visszajáró kiadása címletezve:{Fore.RESET}")
    for cimlet in cimletek:
        db = osszeg // cimlet
        if db > 0:
            egyseg = "bankjegy" if cimlet >= 500 else "érmes"
            print(f"  - {cimlet:>5} Ft-os {egyseg}: {db} db")
            osszeg %= cimlet

def fizetes_es_visszajaro():
    kepernyo_torles()
    print(f"{'='*35}\n{'SZÁMLA ÉS FIZETÉS':^35}\n{'='*35}\n")
    
    total = 0
    van_rendeles = False
    
    for item in menu_elemek:
        if item[0].startswith('Q'):
            continue
            
        nev = item[0][4:]
        db = item[1]
        egyseg_ar = item[2]
        
        if db > 0:
            van_rendeles = True
            resz_osszeg = db * egyseg_ar
            total += resz_osszeg
            print(f"{nev:20} {db:>2} db x {egyseg_ar:>4} Ft = {resz_osszeg:>6} Ft")
    
    if not van_rendeles:
        print("Nem vásároltál semmit. Viszlát!")
        return

    print(f"\n{'='*35}")
    print(f"Fizetendő összeg: {total:>17} Ft")
    print(f"{'='*35}\n")

    bedobott_osszeg = 0
    elfogadott_penzek = [5, 10, 20, 50, 100, 200, 500, 1000, 2000, 5000, 10000, 20000]

    while bedobott_osszeg < total:
        hatralevo = total - bedobott_osszeg
        print(f"Még hiányzik: {Fore.YELLOW}{hatralevo} Ft{Fore.RESET}")
        
        try:
            penz = int(input("Dobj be egy érmét/bankjegyet (Ft): "))
            if penz in elfogadott_penzek:
                bedobott_osszeg += penz
                print(f"{Fore.GREEN}Bedobva: {penz} Ft. Összesen bedobva: {bedobott_osszeg} Ft{Fore.RESET}\n")
            else:
                print(f"{Fore.RED}Az automata ezt az érmét/bankjegyet nem fogadja el!{Fore.RESET}\n")
        except ValueError:
            print(f"{Fore.RED}Kérjük, érvényes összeget adj meg!{Fore.RESET}\n")

    visszajaro = bedobott_osszeg - total
    print(f"{'='*35}")
    print(f"{Fore.GREEN}Sikeres fizetés!{Fore.RESET}")
    print(f"Összes visszajáró: {Fore.CYAN}{visszajaro} Ft{Fore.RESET}")
    
    if visszajaro > 0:
        cimletezes(visszajaro)
    else:
        print("Pontos összeget adtál meg, nincs visszajáró.")
        
    print(f"\n{'='*35}\nKöszönjük a vásárlást! Jó étvágyat!\n")

# PROGRAM FŐCIKLUSA
while True:
    menu()
    valasz = input("Add meg a kiválasztott termék kódját (pl. 10, 30) vagy 'Q' a befejezéshez: ").strip().upper()

    if valasz == "Q":
        fizetes_es_visszajaro()
        break
    else:
        try:
            db = int(input("Hány darabot szeretnél?: "))
            if db > 0:
                rendeles(valasz, db)
            else:
                print(f"{Fore.RED}A darabszámnak legalább 1-nek kell lennie!{Fore.RESET}")
        except ValueError:
            print(f"{Fore.RED}Kérjük, érvényes számot adj meg darabszámnak!{Fore.RESET}")
            
        input("\nÜss Entert a folytatáshoz...")