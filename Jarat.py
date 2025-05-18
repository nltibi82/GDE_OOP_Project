from abc import ABC, abstractmethod
class Jarat(ABC):
    def __init__(self, jaratszam: str, celallomas: str, jegyar: float):
        self.jaratszam = jaratszam
        self.celallomas = celallomas
        self.jegyar = jegyar
    @abstractmethod
    def jarat_info(self):
        pass