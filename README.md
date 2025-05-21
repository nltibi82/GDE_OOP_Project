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

## Használat
Indíts után meg kell adni egy felhasználónevet (ami lehet bármi), ez után egy konzolos menü jelenik meg, ahol a következő opciók közül választhatsz:
- 1 - Járatok Listázása
-	2 – Foglalás: Listázásra kerülnek az eléhető járatok, dátum és járatszám megadása szükséges
-	3 – Foglalás lemondása: Válaszd ki saját foglalásaid közül, melyiket szeretnéd törölni. A törlés a foglalás sorszámának megadásával történik
-	4 – Foglalások listázása: Az összes foglalás megtekintése.
-	5 – Kilépés: A program bezárása.

## Leírás
A program előre feltöltött járatlistával és foglalásokkal rendelkezik. A felhasználó a menüben foglalhat jegyet, lekérdezheti vagy lemondhatja saját foglalásait. A rendszer a dátum alapján ellenőrzi az elérhető járatokat. 

## Készítő
Nádas Tibor
nltibi82@gmail.com
