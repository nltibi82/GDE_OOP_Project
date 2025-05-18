from datetime import datetime
import os
def jaratLista(jaratok: list, legitarsasagok: list):
    print(f"{'Légitársaság':<20}{'Típus':<15}{'Járatszám':<20}{'Célállomás':<20}{'Jegyár (Ft)':<15}")
    print("-" * 100)
    for jarat in jaratok:
        legitarsasag_nev = "Ismeretlen"
        for lt in legitarsasagok:
            if jarat.jaratszam in lt.jaratSzamok:
                legitarsasag_nev = lt.legitarsasagNeve
                break
        info = jarat.jarat_info()
        print(f"{legitarsasag_nev:<20}{info['tipus']:<15}{info['szam']:<20}{info['cel']:<20}{info['ar']:<15}")

def foglalasLista(jaratok: list, legitarsasagok: list, foglalasok: list):
    print(f"{'Sorsz.':<7}{'Név':<20}{'Légitársaság':<20}{'Típus':<15}{'Járatszám':<15}{'Célállomás':<20}{'Jegyár (Ft)':<15}")
    print("-" * 120)
    for index, foglalas in enumerate(foglalasok, 1):
        jarat = None
        legitarsasag_nev = "Ismeretlen"
        jarat_tipus = "Ismeretlen"
        for j in jaratok:
            if j.jaratszam == foglalas.jaratszam:
                jarat = j
                if jarat.__class__.__name__ == "BelfoldiJarat":
                    jarat_tipus = "Belföldi"
                elif jarat.__class__.__name__ == "NemzetkoziJarat":
                    jarat_tipus = "Nemzetközi"
                break
        for lt in legitarsasagok:
            if foglalas.jaratszam in lt.jaratSzamok:
                legitarsasag_nev = lt.legitarsasagNeve
                break
        if jarat:
            print(f"{index:<7}{foglalas.utas_nev:<20}{legitarsasag_nev:<20}"
                  f"{jarat_tipus:<15}{jarat.jaratszam:<15}{jarat.celallomas:<20}{jarat.jegyar:<15}")
        else:
            print(f"{index:<7}{foglalas.utas_nev:<20}{'N/A':<20}{'N/A':<15}"
                  f"{foglalas.jaratszam:<15}{'Járat nem található':<20}{'-':<15}")
            
def foglalas(jaratok: list):
    while True:
        datum_str = input("Add meg a dátumot (ÉÉÉÉ.HH.NN formátumban): ")
        try:
            datum = datetime.strptime(datum_str, "%Y.%m.%d").date()
            if datum < datetime.today().date():
                print("Hibás dátum: nem lehet korábbi, mint a mai nap.")
            else:
                break  
        except ValueError:
            print("Hibás formátum! Kérlek az ÉÉÉÉ.HH.NN formátumot használd.")

    while True:
        keresett_jaratszam = input("Add meg a foglalni kívánt járatszámot: ").strip()
        for jarat in jaratok:
            if jarat.jaratszam == keresett_jaratszam:
                return datum_str, keresett_jaratszam  
        print("Hibás járatszám! Próbáld újra.")
        
def torolFoglalas(foglalasok: list, sorszam: int, felhasznalo: str):
    if 1 <= sorszam <= len(foglalasok):
        foglalas = foglalasok[sorszam - 1]
        if foglalas.utas_nev == felhasznalo:
            torolt = foglalasok.pop(sorszam - 1)
            print(f"Sikeresen törölve: {torolt.utas_nev}, Járat: {torolt.jaratszam}")
        else:
            print("Csak a saját foglalásodat törölheted!")
    else:
        print("Hibás sorszám! Nincs ilyen foglalás.")
def torolKepernyo():
    os.system('cls' if os.name == 'nt' else 'clear')