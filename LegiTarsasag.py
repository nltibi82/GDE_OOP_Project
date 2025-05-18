
class LegiTarsasag:
    def __init__(self, legitarsasagNeve):
        self.legitarsasagNeve= legitarsasagNeve
        self.jaratSzamok=[]
    def jarat_hozzaadas(self, jarat):
        self.jaratSzamok.append(jarat)
    def info(self):
        print(f"Légitársaság: {self.legitarsasagNeve}")
        for szam in self.jaratSzamok:
            print(f"  - {szam}")