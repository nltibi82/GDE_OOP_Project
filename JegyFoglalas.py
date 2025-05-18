class JegyFoglalas:
    def __init__(self, jaratszam: str, utas_nev: str, utazas_datuma):
        self.jaratszam = jaratszam
        self.utas_nev = utas_nev
        self.utazas_datuma= utazas_datuma
    def info(self):
        return f"{self.utas_nev:<20}{self.utazas_datuma:<15}{self.jaratszam:<10}"