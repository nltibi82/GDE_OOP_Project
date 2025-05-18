from Jarat import Jarat
class BelfoldiJarat(Jarat):
    def jarat_info(self):
        return {
            "tipus": "Belföldi",
            "szam": self.jaratszam,
            "cel": self.celallomas,
            "ar": self.jegyar
        }