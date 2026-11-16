# IMPORT
from colorama import Fore, Back, Style
import subprocess


# GLOBÁLIS VÁLTOZÓK
menu_elemek = [["10) Borsodi", 0, 800], 
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
               ["Q) Kilépés", 0, 0]
]

# FÜGGVÉNY DEFINÍCIÓK
def menu():
    subprocess.run(["cls"], shell=True)
    
    print(f"{Fore.RED}Válassz menüt!{Fore.RESET}")
    print(f"{'=' * 40}")
    
    for m in menu_elemek:
        if m[0].startswith('Q'):
            print(f"{m[0]}")
        else:
            print(f"{m[0]:25} {m[2]:>6} Ft")


def rendeles(mit, db):
    i = 0
    while not menu_elemek[i][0].startswith(mit):
         i += 1

    menu_elemek[i][1] += db

def szamla():
    print(f"{'='*35}\n{'SZÁMLA':^35}\n{'='*35}\n")
    
    total = 0
    
    for i in range(len(menu_elemek) - 1):
        nev = menu_elemek[i][0][3:]
        db = menu_elemek[i][1]
        egyseg_ar = menu_elemek[i][2]
        
        if db > 0:
            resz_osszeg = db * egyseg_ar
            total += resz_osszeg
            print(f"{nev:20} {db:>2} db x {egyseg_ar:>4} Ft = {resz_osszeg:>6} Ft")
    
    print(f"\n{'='*35}")
    print(f"Fizetendo osszeg: {total:>17} Ft")
    print(f"{'='*35}")

# ---------------------------

# PROGRAM
menu()

valasz = input("Mit szeretnél?: ").strip().upper()

if valasz == "A":
    db = int(input("Mennyit kér?: "))
    rendeles("A", db)
      
    input("Üss egy billentyűt a folytatáshoz...")
elif valasz == "B":
    db = int(input("Mennyit kér?: "))
    rendeles("B", db)
    
    input("Üss egy billentyűt a folytatáshoz...")
elif valasz == "C":
    db = int(input("Mennyit kér?: "))
    rendeles("C", db)
    
    input("Üss egy billentyűt a folytatáshoz...")
elif valasz == "Q":
    print("Jó étvágyat!")
    szamla()
    exit()


while True:
    menu()

    valasz = input("Mit szeretnél?: ").strip().upper()

    if valasz == "A":
        db = int(input("Mennyit kér?: "))
        rendeles("A", db)
        
        input("Üss egy billentyűt a folytatáshoz...")
    elif valasz == "B":
        db = int(input("Mennyit kér?: "))
        rendeles("B", db)
        
        input("Üss egy billentyűt a folytatáshoz...")
    elif valasz == "C":
        db = int(input("Mennyit kér?: "))
        rendeles("C", db)
        
        input("Üss egy billentyűt a folytatáshoz...")
    elif valasz == "Q":
        print("Jó étvágyat!")
        szamla()
        exit()
menu.py megjelenítése.