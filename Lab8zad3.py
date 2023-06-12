class Graf:
    def __init__(self, liczba_wierzcholkow):
        self.liczba_wierzcholkow = liczba_wierzcholkow
        self.macierz_sasiedztwa = [[0] * liczba_wierzcholkow for _ in range(liczba_wierzcholkow)]

    def dodaj_krawedz(self, u, v):
        if u < 0 or u >= self.liczba_wierzcholkow or v < 0 or v >= self.liczba_wierzcholkow:
            print("Nieprawidłowe wierzchołki.")
            return

        self.macierz_sasiedztwa[u][v] = 1
        self.macierz_sasiedztwa[v][u] = 1

    def drukuj_macierz_sasiedztwa(self):
        print("Macierz sąsiedztwa:")
        for wiersz in self.macierz_sasiedztwa:
            print(wiersz)

    def drukuj_liste_sasiedztwa(self):
        print("Lista sąsiedztwa:")
        for wierzcholek in range(self.liczba_wierzcholkow):
            sasiedzi = [v for v in range(self.liczba_wierzcholkow) if self.macierz_sasiedztwa[wierzcholek][v] == 1]
            print(f"Wierzchołek {wierzcholek}: {sasiedzi}")

    def drukuj_interpretacje_grafu(self):
        print("Interpretacja graficzna:")
        for wiersz in self.macierz_sasiedztwa:
            linia = " ".join(["-" if val == 1 else " " for val in wiersz])
            print(linia)


rodzaj_grafu = input("Podaj rodzaj grafu (skierowany, nieskierowany, ważony itp.): ")
liczba_wierzcholkow = int(input("Podaj liczbę wierzchołków: "))

graf = Graf(liczba_wierzcholkow)

liczba_krawedzi = int(input("Podaj liczbę krawędzi: "))

print("Podaj krawędzie (indeksowane od 0):")
for _ in range(liczba_krawedzi):
    u, v = map(int, input("Podaj krawędź (u v): ").split())
    graf.dodaj_krawedz(u, v)

graf.drukuj_macierz_sasiedztwa()
print()
graf.drukuj_liste_sasiedztwa()
print()
graf.drukuj_interpretacje_grafu()
