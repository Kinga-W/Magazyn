from abc import ABC, abstractmethod
from datetime import datetime


class Raport(ABC):
    @abstractmethod
    def generate_raport(self, **kwargs):
        pass

    def make_file(self, filename, content):
        today = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        with open("data/raports/"+filename+today, "w", encoding="utf-8") as f:
            f.write(content)

class RaportProductsFull(Raport):
    def __init__(self):
        pass

    def generate_raport(self, data):
        header = f"Raport wszystkich produktów\n"

        body = f"{'Nazwa':<40} {'Kod':<15} {'Cena':<10} {'Liczba':<7} {'Jednostka':<10} {'Kategoria':<23} {'Dostawca':<20} {'Opis':<30}\n"
        for p in data:
            body += f"{str(p[0]):<40} {str(p[1]):<15} {str(p[2]):<10} {str(p[3]):<7} {str(p[4]):<10} {str(p[5]):<23} {str(p[6]):<20} {str(p[7]):<30}\n"

        footer = "\nRaport z dnia: " + datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        return header + body + footer

class RaportProductsCat(Raport):
    def __init__(self):
        pass

    def generate_raport(self, data, cat):
        header = f"Raport produktów według kategorii: {cat}\n"

        body = f"{'Nazwa':<40} {'Kod':<15} {'Cena':<10} {'Liczba':<7} {'Jednostka':<10} {'Dostawca':<20} {'Opis':<30}\n"
        for p in data:
            body += f"{str(p[0]):<40} {str(p[1]):<15} {str(p[2]):<10} {str(p[3]):<7} {str(p[4]):<10} {str(p[6]):<20} {str(p[7]):<30}\n"

        footer = "\nRaport z dnia: " + datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        return header + body + footer

class RaportTran(Raport):
    def __init__(self):
        pass

    def generate_raport(self, data):
        header = f"Raport transakcji:\n"

        body = f"{'Data':<10} {'Godzina':<10} {'Produkt':<40} {'Zmiana':<7} {'Operacja':<15} {'Odbiorca/Dostawca':<20}\n"
        for p in data:
            body += f"{str(p[0]):<10} {str(p[1]):<10} {str(p[2]):<40} {str(p[3]):<7} {str(p[4]):<15} {str(p[5]):<20}\n"

        footer = "\nRaport z dnia: " + datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        return header + body + footer