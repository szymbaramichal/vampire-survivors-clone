# Klon gry "Vampire Survivors"

## Opis
Mój projekt to prosty 2D survivalowy shooter stworzony w języku Python przy użyciu biblioteki Pygame. Gracz steruje postacią, która musi przetrwać ataki wrogów i unikać kolizji z przeszkodami na planszy.

## Wymagania
Aby uruchomić projekt lokalnie, należy spełnić następujące wymagania:
- Python 3.x zainstalowany na systemie
- Biblioteka Pygame zainstalowana (`pip install pygame`)

## Uruchomienie
1. Sklonuj repozytorium na swój lokalny komputer.
2. Uruchom terminal w głównym katalogu projektu.
3. Uruchom plik `main.py` za pomocą Pythona: `python main.py`.
4. Gra rozpocznie się po kliknięciu Play na ekranie

## Użyte Technologie
- Python 3.x
- Pygame - biblioteka do tworzenia gier w Pythonie
- Pytmx - biblioteka do ładowania i przetwarzania plików TMX (Tile Map XML) używanych do tworzenia map w grach 2D
- Tiled - program do edycji poziomów

## Struktura Projektu
- **main.py**: Główny plik programu, zawierający logikę gry i jej uruchomienie.
- **player.py**: Moduł zawierający klasę gracza i jego logikę.
- **sprites.py**: Moduł zawierający klasy sprite'ów, takie jak pociski, wrogowie i obiekty kolizyjne.
- **groups.py**: Moduł zawierający grupy sprite'ów używane w grze.
- **settings.py**: Moduł zawierający stałe i ustawienia gry, takie jak rozmiar okna i rozmiar kafelka.
- **images/**: Katalog zawierający grafiki używane w grze.
- **audio/**: Katalog zawierający pliki dźwiękowe używane w grze.
- **data/**: Katalog zawierający dane gry, takie jak mapy.
