## Repülőjegy Foglalási Rendszer

Egy egyszerű konzolos repülőjegy foglalási rendszer Pythonban. A program lehetőséget nyújt belföldi és nemzetközi járatok kezelésére, valamint jegyfoglalásra, lemondásra és foglalások listázására.

### Előfeltételek:
Python 3.7, egyéb kiegészítők nem szükségesek.

### Futtatás:
1.	Klónozd vagy töltsd le a projektet: https://github.com/nltibi82/GDE_OOP_Project

2.	Futtasd a fő programot: main.py

## Felépítés
 - **Jarat.py (absztrakt osztály):** Definiálja a járat alapvető attribútumait (járatszám, célállomás, jegyár).
 - **NemzetkoziJarat.py (származtatott osztály):** Nemzetközi járatok
 - **BelfoldiJarat.py (származtatott osztály):** Belföldi járatok
 - **LegiTarsasag.py:** Légi társaságokat megvalósító osztály
 - **JegyFoglalas.py:** A jegyek foglalását megvalósító osztály
 - **megjelenites.py:** A megjelenítésért felelős eljárások
 - **muveletek.py:** A adatokon műveleteket végző eljárások
 - **adatFeltoltes.py:** Alapadatok feltöltése
 - **main.py** Főprogram
