import sys


class Graf:
    def __init__(self, liczba_wierzcholkow):
        self.liczba_wierzcholkow = liczba_wierzcholkow
        self.macierz_sasiedztwa = [[0] * liczba_wierzcholkow for _ in range(liczba_wierzcholkow)]

    def dodaj_krawedz(self, u, v, waga):
        self.macierz_sasiedztwa[u][v] = waga

    def najkrotsza_droga(self, zrodlo):
        odleglosci = [sys.maxsize] * self.liczba_wierzcholkow
        odleglosci[zrodlo] = 0
        odwiedzone = set()

        while len(odwiedzone) < self.liczba_wierzcholkow:
            u = min((wierzcholek for wierzcholek in range(self.liczba_wierzcholkow) if wierzcholek not in odwiedzone),
                    key=lambda x: odleglosci[x])
            odwiedzone.add(u)

            for v in range(self.liczba_wierzcholkow):
                if self.macierz_sasiedztwa[u][v] > 0 and v not in odwiedzone:
                    odleglosc = odleglosci[u] + self.macierz_sasiedztwa[u][v]
                    if odleglosc < odleglosci[v]:
                        odleglosci[v] = odleglosc

        return odleglosci


graf = Graf(5)

graf.dodaj_krawedz(0, 1, 4)
graf.dodaj_krawedz(0, 2, 1)
graf.dodaj_krawedz(1, 2, 2)
graf.dodaj_krawedz(1, 3, 5)
graf.dodaj_krawedz(2, 3, 1)
graf.dodaj_krawedz(2, 4, 3)
graf.dodaj_krawedz(3, 4, 2)

zrodlo = 0
najkrotsze_drogi = graf.najkrotsza_droga(zrodlo)

print(f"Najkrótsze drogi z wierzchołka {zrodlo}:")
for wierzcholek, odleglosc in enumerate(najkrotsze_drogi):
    print(f"Do wierzchołka {wierzcholek}: {odleglosc}")
