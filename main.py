from JegyFoglalas import JegyFoglalas
from adatFeltoltes import adatFeltoltesJaratok, adatFeltoltesJegyFoglalas, adatFeltoltesLegitarsasagok
from megejelnites import alapFejlec, kepernyoMenu, alapLablec
from muveletek import jaratLista, foglalasLista, foglalas, torolFoglalas, torolKepernyo

foglalasok = adatFeltoltesJegyFoglalas()
legitarsasagok = adatFeltoltesLegitarsasagok()
jaratok = adatFeltoltesJaratok()
torolKepernyo()
alapFejlec("Repülőjegy Foglalási Rendszer")
felhasznalo = input("Felhasználó név: " )
while True:
    torolKepernyo()
    alapFejlec("Repülőjegy Foglalási Rendszer")
    kepernyoMenu(felhasznalo)
    alapLablec(felhasznalo)
    valasztas = input(f"Válassz egy menüpontot {felhasznalo}(1-5): ")
    if valasztas=="1":
        torolKepernyo()
        alapFejlec("Repülő járatok")
        jaratLista(jaratok,legitarsasagok)
        alapLablec(felhasznalo)
        input("\n A folytatáshoz nyomd meg az ENTER gombot...")
    elif valasztas=="2":
        torolKepernyo()
        alapFejlec("Foglalás")
        jaratLista(jaratok,legitarsasagok)
        alapLablec(felhasznalo)
        datum, jaratszam = foglalas(jaratok)
        foglalasok.append(JegyFoglalas(jaratszam,felhasznalo,datum))
        print("A foglalás sikeres!")
        input("\n A folytatáshoz nyomd meg az ENTER gombot...")
    elif valasztas=="3":
        while True:
            torolKepernyo()
            alapFejlec("Törlés")
            foglalasLista(jaratok,legitarsasagok,foglalasok)
            sorszam = int(input("Add meg a törölni kívánt foglalás sorszámát: "))
            torolFoglalas(foglalasok, sorszam, felhasznalo)
            muvelet=input("Szeretnél egy másik foglalást törölni? (I/N): ")
            if (muvelet=='n') or (muvelet=='N'):
                break
            else:
                if muvelet !='i' or muvelet !='I':
                    print("Nem megfelelő karaktert adtál meg!")
    elif valasztas=="4":
        torolKepernyo()
        alapFejlec("Foglalások")
        foglalasLista(jaratok,legitarsasagok,foglalasok)
        alapLablec(felhasznalo)
        input("\n A folytatáshoz nyomd meg az ENTER gombot...")
    elif valasztas=="5":
        print("Köszönjük a látogatást!")
        break
    else:
        print("Érvénytelen választás. Kérlek 1 és 5 között adj meg számot.")