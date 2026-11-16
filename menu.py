#import
from colorama import Fore, Back, Style
import random
import subprocess
#globalis valtozok

#fuggveny definiciok
def menu():
    subprocess.run(["cls"], shell=True)

    print(f"{Fore.RED} Válassz menut!{Fore.RESET}")
    print("A) Big MAc")
    print("B) Pörkölt nokedlivel")
    print("C) Big Tasty")
    print("Q) EXIT")


# -------------------------------

#program

print(f"{Fore.BLUE}Válassz menüt:")
print("A) Big MAc")
print("B) Pörkölt nokedlivel")
print("C) Big Tasty")
print("Q) EXIT")
print("----------------------------------")


valasz=input("Mit szeretnél?:  ")
osszeg=0
    
while valasz != "Q":
    subprocess.run(["cls"], shell=True)
    if valasz == "A":
        print(f"{Fore.YELLOW}500 Ft{Fore.RESET}")
        osszeg += 500
    elif valasz == 'B':
        print(f"{Fore.YELLOW}1000 Ft{Fore.RESET}")
        osszeg += 1000
    elif valasz == 'C':
        print(f"{Fore.YELLOW}2000 Ft{Fore.RESET}")
        osszeg += 2000
    else:
        print("Elirtad kutyaa")
    print(f"{Fore.RED}Válassz menüt!{Fore.RESET}")
    print(f"A) Big Mac menü")
    print("B) Pörkölt nokedlival")
    print("C) Big Tasty")
    print("Q) Exit")
    print("---------------------------------")
    valasz = input("Mit szeretnél?: ")

