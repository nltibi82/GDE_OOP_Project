from NemzetkoziJarat import NemzetkoziJarat
from BelfoldiJarat import BelfoldiJarat
from JegyFoglalas import JegyFoglalas
from LegiTarsasag import LegiTarsasag

def adatFeltoltesJaratok():
    jarat=[]
    jarat.append(NemzetkoziJarat("1050","Tokio",620000))
    jarat.append(NemzetkoziJarat("1080","New York",480000))
    jarat.append(NemzetkoziJarat("1020","London",310000))
    jarat.append(BelfoldiJarat("2010","Debrecen",55000))
    jarat.append(BelfoldiJarat("2040","Miskolc",65000))
    jarat.append(BelfoldiJarat("2070","Zalaegerszeg",59000))
    return jarat
def adatFeltoltesLegitarsasagok():
    lt=[]
    wizzair=LegiTarsasag("WizzAir")
    malev=LegiTarsasag("Malév")
    wizzair.jarat_hozzaadas("1050")
    wizzair.jarat_hozzaadas("1080")
    wizzair.jarat_hozzaadas("1020")
    malev.jarat_hozzaadas("2010")
    malev.jarat_hozzaadas("2040")
    malev.jarat_hozzaadas("2070")
    lt.append(wizzair)
    lt.append(malev)
    return lt
def adatFeltoltesJegyFoglalas():
    foglalasok = []
    foglalasok.append(JegyFoglalas("1050", "Kovács Anna", "2025.10.17"))
    foglalasok.append(JegyFoglalas("1080", "Szabó Péter", "2025.11.09"))
    foglalasok.append(JegyFoglalas("2010", "Varga Kitti", "2025.09.28"))
    foglalasok.append(JegyFoglalas("2010", "Kis Imre", "2025.09.28"))
    foglalasok.append(JegyFoglalas("2040", "Nagy Ferenc", "2025.10.05"))
    foglalasok.append(JegyFoglalas("1020", "Kovács Mária", "2025.09.28"))
    return foglalasok


