from Jarat import Jarat
class NemzetkoziJarat(Jarat):
    def jarat_info(self):
        return {
            "tipus": "Nemzetközi",
            "szam": self.jaratszam,
            "cel": self.celallomas,
            "ar": self.jegyar
        }